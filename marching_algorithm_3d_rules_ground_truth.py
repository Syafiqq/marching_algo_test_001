import numpy as np
import pyvista as pv

import math
import marching_3d_rules_minimal as rules

nz_dims = 2
nxy_dims = 3

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
xyz_selection_probability = np.array([
    xyz_points[21],
    xyz_points[22],
    xyz_points[25],
    xyz_points[26],
    xyz_points[37],
    xyz_points[38],
    xyz_points[41],
    xyz_points[42],
])


# --------


looper = []
for i in np.arange(1, 255, 1, dtype=np.int):
    str = f'{i:08b}'
    arr = [
        int(str[0]),
        int(str[1]),
        int(str[2]),
        int(str[3]),
        int(str[4]),
        int(str[5]),
        int(str[6]),
        int(str[7]),
    ]
    looper.append([i, np.sum(arr), arr, str])
looper = sorted(looper, key=lambda x: (x[1], x[0]))


# --------

loop_whitelist = []
use_whitelist = False

for iter, loop in enumerate(looper):
    if use_whitelist and loop[0] not in loop_whitelist:
        continue
    xyz_points_object = []
    obj_point = loop[2]
    for i, point in enumerate(obj_point):
        if point == 1:
            xyz_points_object.append(xyz_selection_probability[i])


# --------


    def contains(list, filter):
        for x in list:
            if filter(x):
                return True
        return False


    object_index = []
    for point in xyz_points:
        if contains(xyz_points_object, lambda x: (x == point).all()):
            object_index.append(1)
        else:
            object_index.append(0)


# --------

    xyz_points_lines = []
    for point in [[21, 22], [22, 26], [25, 26], [21, 25], [37, 38], [38, 42], [37, 41], [41, 42], [21, 37], [22, 38], [25, 41], [26, 42]]:
        if object_index[point[0]] == 1 and object_index[point[0]] == object_index[point[1]]:
            xyz_points_lines.append([xyz_points[point[0]], xyz_points[point[1]]])


# --------


    def num_digits(n):
        if n > 0:
            digits = int(math.log10(n)) + 1
        elif n == 0:
            digits = 1
        else:
            digits = int(math.log10(-n)) + 2
        return digits

    dictionary = {}
    points_p = []
    faces_p = []

    digit_x = 10 ** (num_digits(nxy_ratio_dims) + 1)
    digit_y = 10 ** (num_digits(nxy_ratio_dims) + 1)

    max_z = digit_x * digit_y
    max_y = digit_x

    cxy = xyz_dims[0] * xyz_dims[1]
    cx = xyz_dims[0]
    cxy_plus1 = xyz_dims_plus1[0] * xyz_dims_plus1[1]
    cx_plus1 = xyz_dims_plus1[0]

    variant = 2

    for i in np.arange(0, np.prod(xyz_dims), 1, dtype=np.int):
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

        point_type = (object_index[p0] << 7) + (object_index[p1] << 6) + (object_index[p2] << 5) + (object_index[p3] << 4) + (object_index[p4] << 3) + (object_index[p5] << 2) + (object_index[p6] << 1) + (object_index[p7] << 0)
        point_group = [
            xyz_points[p0],
            xyz_points[p1],
            xyz_points[p2],
            xyz_points[p3],
            xyz_points[p4],
            xyz_points[p5],
            xyz_points[p6],
            xyz_points[p7],
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


# --------
# GIF CREATION

#    polyline = pv.PolyData(points_p, faces=np.array(faces_p).flatten()).triangulate()
#    print(f'{iter+1:0>4}', f'{loop[0]: >4}', loop[3], polyline.is_manifold, polyline.is_all_triangles())
#    filename = f'{iter+1:0>4}-{loop[3]}'
#    polyline.save(f'marching-algorithm-3d-rules-ground-truth-stl/dump/{filename}.stl')

#    plot = pv.Plotter(notebook=False, off_screen=True)
#    plot.add_points(xyz_points, show_edges=True)
#    plot.add_points(np.array(xyz_points_object), scalars=np.array(xyz_points_object), cmap=['red'], render_points_as_spheres=True, point_size=20.0)
#    for line in xyz_points_lines:
#        plot.add_lines(np.array(line), color='red', width=20)
#    plot.add_mesh(polyline, color=None, opacity=0.9, show_edges=False)
#    plot.show_bounds()
#    plot.show_grid()
#    plot.remove_scalar_bar()
#    plot.open_gif(f'marching-algorithm-3d-rules-ground-truth/{filename}.gif')
#
#    for elevation in [90.0, 60.0, 30.0, 0.0, -30.0, -60.0, -90.0]:
#        for azimuth in [0.0, 30.0, 60.0, 90.0, 120.0, 150.0, 180.0, 210.0, 240.0, 270.0, 300.0, 330.0, 360.0]:
#            plot.camera_position = 'xz'
#            plot.camera.azimuth = azimuth
#            plot.camera.elevation = elevation
#            plot.write_frame()
#    plot.close()

# --------
# MANIFOLD AND TRIANGLES ONLY CHECKING

#    polyline = pv.PolyData(points_p, faces=np.array(faces_p).flatten())
#    print(f'{iter+1:0>4}', f'{loop[0]: >4}', loop[3], polyline.is_manifold, polyline.is_all_triangles())


# --------
# LIVE PREVIEW

#    plot = pv.Plotter(notebook=False, off_screen=False)
#    plot.add_points(xyz_points, show_edges=True)
#    plot.add_points(np.array(xyz_points_object), scalars=np.array(xyz_points_object), cmap=['red'], render_points_as_spheres=True, point_size=20.0)
#    for line in xyz_points_lines:
#        plot.add_lines(np.array(line), color='red', width=20)
#    plot.add_mesh(polyline, color=None, opacity=0.9, show_edges=False)
#    plot.show_bounds()
#    plot.show_grid()
#    plot.remove_scalar_bar()
#    plot.camera_position = 'yz'
#    plot.camera.azimuth = -45.0
#    plot.camera.elevation = 30.0
#    plot.show()

# --------