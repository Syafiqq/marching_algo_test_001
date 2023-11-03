import numpy as np
import pyvista as pv
import cv2 as cv
from matplotlib.path import Path
import matplotlib.patches as patches
from shapely.geometry import Polygon, MultiPolygon, Point

from marching_cube_metadata import MarchingCubeMetadata


def generate(input_paths: [str], xy_size: int) -> ([int], MarchingCubeMetadata):
    # Define The Grid
    nz_dims = len(input_paths)
    nxy_dims = xy_size

    nz_ratio_dims = nz_dims + 1
    nxy_ratio_dims = int(nxy_dims * 1)

    xyz_dims = np.array([nxy_ratio_dims, nxy_ratio_dims, nz_ratio_dims])
    xyz_dims_plus1 = [xyz_dims[0] + 1, xyz_dims[1] + 1, xyz_dims[2] + 1]

    xyz_spacing = (nxy_dims / xyz_dims[0], nxy_dims / xyz_dims[1], 1)
    xyz_grid = pv.UniformGrid(
        dims=xyz_dims_plus1,
        spacing=xyz_spacing,
        origin=(0, 0, 0),
    )

    xyz_points = np.transpose(xyz_grid.points.T)

    # Find contour points
    stacked_contour_points = []
    for name in input_paths:
        image_memory = cv.imread(name)
        inverted_image = cv.bitwise_not(image_memory)
        img_gray = cv.cvtColor(inverted_image, cv.COLOR_BGR2GRAY)
        ret, thresh = cv.threshold(img_gray, 150, 255, cv.THRESH_BINARY)
        im2, contours, hierarchy = cv.findContours(image=thresh, mode=cv.RETR_TREE, method=cv.CHAIN_APPROX_NONE)

        multi_points = []
        for contour in contours:
            contour_points = contour[:, 0]
            path = Path(contour_points, closed=True)
            patch = patches.PathPatch(path, facecolor=None, lw=1, antialiased=True)
            vertices = patch.get_path().vertices
            trans = patch.get_patch_transform()
            points = trans.transform(vertices)
            multi_points.append(points)
        stacked_contour_points.append(multi_points)
    stacked_contour_points.insert(0, [])
    stacked_contour_points.append([])

    # Define point clouds
    object_index = []
    xyz_points_object = []
    for z in np.arange(0, xyz_dims_plus1[2], 1):
        multi_multipolygon = []
        for points in stacked_contour_points[z]:
            if len(points) <= 2:
                continue
            poly = Polygon(points)
            poly_big = poly.buffer(1e-6)
            if poly_big.geom_type == 'MultiPolygon':
                pass
            elif poly_big.geom_type == 'Polygon':
                poly_big = MultiPolygon([poly_big])
            else:
                pass
            multi_multipolygon.append(poly_big)

        for i, o in enumerate(np.array(list(filter(lambda c: c[2] == z, xyz_points)))):
            point = Point(o[:2])
            inserted = False
            for multipolygon in multi_multipolygon:
                if multipolygon.contains(point):
                    xyz_points_object.append(o)
                    inserted = True
                    break
            object_index.append(1 if inserted else 0)

    return (
        object_index,
        MarchingCubeMetadata(
            nz_dims,
            nxy_dims,
            nz_ratio_dims,
            nxy_ratio_dims,
            xyz_dims,
            xyz_dims_plus1,
            xyz_points
        )
    )
