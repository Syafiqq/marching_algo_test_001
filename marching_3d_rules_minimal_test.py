import numpy as np
import pyvista as pv
import marching_3d_rules_minimal as rules

points = np.array(
    [
        [10, 10, 10],
        [20, 10, 10],
        [10, 20, 10],
        [20, 20, 10],
        [10, 10, 20],
        [20, 10, 20],
        [10, 20, 20],
        [20, 20, 20],
    ]
    , dtype=np.float)

types = [
    0b00111101,
]
variant = 1

polyses = []
for type in types:
    rule_type = type
    points_r = rules.to_points(points, rule_type, variant=variant)
    print(points_r)
    faces_r = rules.to_faces(np.arange(0, len(points_r), 1), rule_type, variant=variant)
    cloud = pv.PolyData(points_r, faces=faces_r)
    polyses.append(cloud)

plot = pv.Plotter()
plot.add_points(points)
for poly in polyses:
    plot.add_mesh(poly, show_edges=True, edge_color='r')
plot.show_bounds()
plot.show_grid()
plot.camera_position = 'yz'
plot.camera.azimuth = -45.0
plot.camera.elevation = 30.0
plot.show(auto_close=True)

