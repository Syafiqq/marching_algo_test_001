import numpy as np
import pyvista as pv

import math
import marching_3d_rules_minimal as rules

xyz_grid = pv.UniformGrid(
    dims=(2, 2, 2),
    spacing=(1, 1, 1),
    origin=(0, 0, 0),
)

xyz_points = np.transpose(xyz_grid.points.T)


def to_scalars(p):
    return (p[0] * (10 ** 1)) + (p[1] * (10 ** 2)) + (p[2] * (10 ** 3))


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

variant = 1

looper_whitelist = [
    0b01100100
]
should_execute_whitelist = False

for iter, loop in enumerate(looper):
    if should_execute_whitelist and loop[0] not in looper_whitelist:
        continue
    p_points = rules.to_points(xyz_points, loop[0], variant=variant)
    p_faces = rules.to_faces(p_points, loop[0], variant=variant)
    p_scalar_2 = [x[-3:] for x in np.reshape(p_faces, (-1, 4))]
    p_scalars = [[to_scalars(z) for z in y] for y in p_scalar_2]
    p_scalars_sorted = sorted(p_scalars, key=lambda e: (e[0], e[1], e[2]))
    is_per_item_sorted = all(x == sorted(x) for x in p_scalars)
    is_cumulative_sorted = p_scalars == p_scalars_sorted
    print(f'{iter+1:0>4}', loop[3], is_per_item_sorted, is_cumulative_sorted)