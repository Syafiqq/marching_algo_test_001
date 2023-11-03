from dataclasses import dataclass
import numpy as np


@dataclass
class MarchingCubeMetadata:
    nz_dims: int
    nxy_dims: int
    nz_ratio_dims: int
    nxy_ratio_dims: int
    xyz_dims: [int]
    xyz_dims_plus1: [int]
    xyz_points: np.ndarray
