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
print(xyz_points)


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

for iter, loop in enumerate(looper):
    p_points = rules.to_points(xyz_points, loop[0], variant=variant)
    p_scalar = [to_scalars(p) for p in p_points]
    print(f'{iter+1:0>4}', loop[3], p_scalar == sorted(p_scalar))