import struct
from marching_cube_metadata import MarchingCubeMetadata
from typing import Callable


def build_with_header(
        values: [int],
        metadata: MarchingCubeMetadata,
        output_path: str,
        value_generator: Callable[[], int]
):
    with open(output_path, "wb") as fp:
        fp.write(struct.pack(
            "<HHH",
            metadata.xyz_dims_plus1[0],
            metadata.xyz_dims_plus1[1],
            metadata.xyz_dims_plus1[2])
        )
        for object_i in values:
            if object_i == 0:
                fp.write(struct.pack("<H", 0))
            else:
                fp.write(struct.pack("<H", value_generator()))


def build_without_header(
        values: [int],
        output_path: str,
        value_generator: Callable[[], int]
):
    with open(output_path, "wb") as fp:
        for object_i in values:
            if object_i == 0:
                fp.write(struct.pack("<H", 0))
            else:
                fp.write(struct.pack("<H", value_generator()))
