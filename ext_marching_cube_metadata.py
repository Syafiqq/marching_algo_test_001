from marching_cube_metadata import MarchingCubeMetadata


def debug_metadata(metadata: MarchingCubeMetadata):
    print('nz_dims', metadata.nz_dims)
    print('nxy_dims', metadata.nxy_dims)
    print('nz_ratio_dims', metadata.nz_ratio_dims)
    print('nxy_ratio_dims', metadata.nxy_ratio_dims)
    print('xyz_dims', metadata.xyz_dims)
    print('xyz_dims_plus1', metadata.xyz_dims_plus1)
    print('xyz_points.shape', metadata.xyz_points.shape)
