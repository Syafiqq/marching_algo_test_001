import numpy as np
import pyvista as pv

from marching_cube_metadata import MarchingCubeMetadata


def generate_by_array(values: [int], xy_size: int, z_size: int) -> ([int], MarchingCubeMetadata):
    # Define The Grid
    input_val = values

    xyz_dims_plus1 = [xy_size, xy_size, z_size]
    xyz_dims = [xyz_dims_plus1[0] - 1, xyz_dims_plus1[1] - 1, xyz_dims_plus1[2] - 1]

    nxy_ratio_dims = xyz_dims[0]  # xyz_dims[1]
    nz_ratio_dims = xyz_dims[2]

    nz_dims = nz_ratio_dims - 1
    nxy_dims = nxy_ratio_dims

    xyz_spacing = (nxy_dims / xyz_dims[0], nxy_dims / xyz_dims[1], 1)
    xyz_grid = pv.UniformGrid(
        dims=xyz_dims_plus1,
        spacing=xyz_spacing,
        origin=(0, 0, 0),
    )

    xyz_points = np.transpose(xyz_grid.points.T)

    return (
        input_val,
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


def generate_by_input(input_path: str, xy_size: int, z_size: int) -> ([int], MarchingCubeMetadata):
    # Define The Grid
    input_val = np.loadtxt(input_path, dtype=int)
    return generate_by_array(input_val, xy_size, z_size)
