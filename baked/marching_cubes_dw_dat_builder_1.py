import point_clouds_generator_stacked_image as generator
import ext_marching_cube_metadata as metadata_debugger
import dat_builder
from typing import Callable


def main(input_paths: [str], output_path: str, xy_size: int, value_generator: Callable[[], int]):
    values, metadata = generator.generate(input_paths, xy_size)

    metadata_debugger.debug_metadata(metadata)

    dat_builder.build_with_header(values, metadata, output_path, value_generator)


if __name__ == "__main__":
    pass
