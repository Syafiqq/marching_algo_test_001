import numpy as np
import pyvista
import pyvista as pv

import math
import marching_3d_rules_minimal as rules

nz_dims = 1
nxy_dims = 1

nz_ratio_dims = nz_dims
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
xyz_selection_probability = xyz_points

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

def to_scalars(p):
    return (p[0] * (10 ** 1)) + (p[1] * (10 ** 2)) + (p[2] * (10 ** 3))


def to_scalar_faces(p_points, p_faces):
    p_faces_no_dimension = [x[-3:] for x in np.reshape(p_faces, (-1, 4))]
    p_faces_points = [map(lambda i: p_points[i], x) for x in p_faces_no_dimension]
    p_faces_points = [list(x) for x in p_faces_points]
    p_faces_scalar = [[to_scalars(p) for p in tri] for tri in p_faces_points]
    return [sorted(x) for x in p_faces_scalar]


def to_faces_midpoint(p_points, p_faces):
    p_faces_no_dimension = [x[-3:] for x in np.reshape(p_faces, (-1, 4))]
    p_faces_points = [map(lambda i: p_points[i], x) for x in p_faces_no_dimension]
    p_faces_points = [list(x) for x in p_faces_points]
    p_faces_center_points = [[center_of_two_points(x[0], x[1]), center_of_two_points(x[1], x[2]), center_of_two_points(x[2], x[0])] for x in p_faces_points]
    return [sorted(x, key=lambda x: (x[0], x[1], x[2])) for x in p_faces_center_points]


def center_of_two_points(p1, p2):
    return [(p1[0] + p2[0]) / 2.0, (p1[1] + p2[1]) / 2.0, (p1[2] + p2[2]) / 2.0]


loop_whitelist = []
use_whitelist = False
compacter = [
    #0, key
    #1, mesh,
    #2, loop
    #3. accumulated key
    #4. ordered mesh points
]

variant = 1

for iter, loop in enumerate(looper):
    if use_whitelist and loop[0] not in loop_whitelist:
        continue
    xyz_points_object = []
    obj_point = loop[2]
    for i, point in enumerate(obj_point):
        if point == 1:
            xyz_points_object.append(xyz_selection_probability[i])
    obj_point = loop[2]

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

    polyline = pv.PolyData(points_p, faces=np.array(faces_p).flatten())
    found = False

    for zdir in [0, 90, 180, 270]:
        if found:
            continue
        else:
            for ydir in [0, 90, 180, 270]:
                if found:
                    continue
                else:
                    for xdir in [0, 90, 180, 270]:
                        if found:
                            continue
                        else:
                            rotated_polyline = polyline.rotate_x(xdir, point=(0.5, 0.5, 0.5), inplace=False)
                            rotated_polyline = rotated_polyline.rotate_y(ydir, point=(0.5, 0.5, 0.5), inplace=False)
                            rotated_polyline = rotated_polyline.rotate_z(zdir, point=(0.5, 0.5, 0.5), inplace=False)
                            rotated_polyline = pyvista.PolyData(np.around(rotated_polyline.points, decimals=1), faces=rotated_polyline.faces)
                            p_faces_center_points = to_faces_midpoint(p_points=np.array(rotated_polyline.points), p_faces=rotated_polyline.faces)

                            for i, compact in enumerate(compacter):
                                if len(compact[4]) == len(p_faces_center_points):
                                    if all(any(q == p for q in compact[4]) for p in p_faces_center_points):
                                        compacter[i][3].append(loop[3])
                                        found = True
                                        break

    if not found:
        compacter.append(
            [
                loop[3],
                polyline,
                loop,
                [loop[3]],
                to_faces_midpoint(p_points=np.array(polyline.points), p_faces=polyline.faces),
            ]
        )


for compact in compacter:
    a = 10
# Attempt 1
#
#    points = np.array(
#        [
#            [10, 10, 10],
#            [20, 10, 10],
#            [10, 20, 10],
#            [20, 20, 10],
#            [10, 10, 20],
#            [20, 10, 20],
#            [10, 20, 20],
#            [20, 20, 20],
#        ]
#        ,dtype=np.float
#    )
#
#    rule_type = int(f'0b{compact[0]}', 2)
#    points_r = rules.to_points(points, rule_type, variant=variant)
#    faces_r = rules.to_faces(np.arange(0, len(points_r), 1), rule_type, variant=variant)
#    cloud = pv.PolyData(points_r, faces=faces_r)
#
#    plot = pv.Plotter(off_screen=True)
#    plot.add_points(points)
#    plot.add_mesh(cloud, show_edges=True, edge_color='r')
#    plot.show_bounds()
#    plot.show_grid()
#    plot.camera_position = 'yz'
#    plot.camera.azimuth = -45.0
#    plot.camera.elevation = 30.0
#    plot.show(screenshot=f'marching_algorithm_3d_rules_compacter/v1/0b{compact[0]}.png')
#
# Attempt 2
#    print(f'0b{compact[0]}', ' '.join(map(lambda x: f'0b{x}', compact[3])))
