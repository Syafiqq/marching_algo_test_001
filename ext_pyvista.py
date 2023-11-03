import pyvista as pv


def debug_polyline(polyline: pv.PolyData):
    print('is_all_triangles', polyline.is_all_triangles)
    print('is_manifold', polyline.is_manifold)
    print('n_faces', polyline.n_faces)
    print('n_cells', polyline.n_cells)
    print('n_lines', polyline.n_lines)
    print('n_points', polyline.n_points)
    print('n_open_edges', polyline.n_open_edges)
    print('n_verts', polyline.n_verts)
