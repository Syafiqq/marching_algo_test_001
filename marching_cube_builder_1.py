import numpy as np
import common
import ext_marching_cube_metadata
from marching_cube_metadata import MarchingCubeMetadata
import marching_3d_rules_minimal as rules
import pyvista as pv


def build(
        values: [int],
        metadata: MarchingCubeMetadata,
        output_path: str,
        variant: int,
        display_result: bool
) -> pv.PolyData:
    dictionary = {}
    points_p = []
    faces_p = []

    digit_x = 10 ** (common.num_digits(metadata.nxy_ratio_dims) + 1)
    digit_y = 10 ** (common.num_digits(metadata.nxy_ratio_dims) + 1)

    max_z = digit_x * digit_y
    max_y = digit_x

    cxy = metadata.xyz_dims[0] * metadata.xyz_dims[1]
    cx = metadata.xyz_dims[0]
    cxy_plus1 = metadata.xyz_dims_plus1[0] * metadata.xyz_dims_plus1[1]
    cx_plus1 = metadata.xyz_dims_plus1[0]

    for i in np.arange(0, np.prod(metadata.xyz_dims), 1, dtype=np.int):
        # @formatter:off
        dz = i // cxy                                       # i div (dimension x and y) to get axis z
        dz_r = i - (dz * cxy)                               # get the remaining of dz
        dy = dz_r // cx                                     # remain of dz div (dimension of x) to get axis y
        dy_r = dz_r - (dy * cx)                             # get the remaining of dy
        dx = dy_r                                           # get the dx

        pt = dz * cxy_plus1 + dy * cx_plus1 + dx * 1        # mapping value to match array of points
        p0 = pt                                             # find the lowest x
        p1 = pt + 1                                         # find the lowest x + 1
        p2 = p0 + cx_plus1                                  # find the lowest x with y + 1
        p3 = p1 + cx_plus1                                  # find the lowest x + 1 with y + 1

        p4 = p0 + cxy_plus1
        p5 = p1 + cxy_plus1
        p6 = p2 + cxy_plus1
        p7 = p3 + cxy_plus1
        # @formatter:on

        point_type = (
                (np.sign(values[p0]) << 7) +
                (np.sign(values[p1]) << 6) +
                (np.sign(values[p2]) << 5) +
                (np.sign(values[p3]) << 4) +
                (np.sign(values[p4]) << 3) +
                (np.sign(values[p5]) << 2) +
                (np.sign(values[p6]) << 1) +
                (np.sign(values[p7]) << 0)
        )

        point_group = [
            metadata.xyz_points[p0],
            metadata.xyz_points[p1],
            metadata.xyz_points[p2],
            metadata.xyz_points[p3],
            metadata.xyz_points[p4],
            metadata.xyz_points[p5],
            metadata.xyz_points[p6],
            metadata.xyz_points[p7],
        ]
        poly_points = rules.to_points(point_group, point_type, variant=variant)
        position = []
        for poly_point in poly_points:
            magnitude = poly_point[0] + (max_y * (poly_point[1] + 1)) + (max_z * (poly_point[2] + 1))
            if dictionary.get(magnitude) is None:
                points_p.append(poly_point)
                dictionary[magnitude] = len(points_p) - 1
            position.append(dictionary[magnitude])
        for poly_face in rules.to_faces(position, point_type, variant=variant):
            faces_p.append(poly_face)

    polyline = pv.PolyData(points_p, faces=np.array(faces_p).flatten())

    polyline.save(output_path)

    if display_result:
        plot = pv.Plotter()
        plot.add_mesh(polyline, show_edges=True)
        plot.camera_position = 'xy'
        plot.show_bounds()
        plot.show_grid()
        plot.camera_position = 'yz'
        plot.camera.azimuth = -45.0
        plot.camera.elevation = 30.0
        plot.show()

    return polyline
