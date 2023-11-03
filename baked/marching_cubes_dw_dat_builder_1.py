import random

import point_clouds_generator_stacked_image as generator
import ext_marching_cube_metadata as metadata_debugger
import dat_builder
from typing import Callable


def main(input_paths: [str], output_path: str, xy_size: int, value_generator: Callable[[], int]):
    values, metadata = generator.generate(input_paths, xy_size)

    metadata_debugger.debug_metadata(metadata)

    dat_builder.build_with_header(values, metadata, output_path, value_generator)


def example_sq_object():
    main(
        [
            '../images/sq-object/sq-0001.png',
            '../images/sq-object/sq-0002.png',
            '../images/sq-object/sq-0003.png',
            '../images/sq-object/sq-0004.png',
            '../images/sq-object/sq-0005.png',
            '../images/sq-object/sq-0006.png',
        ],
        '../input/sq_object.dat',
        20,
        lambda: 1
    )


def example_oas_1():
    main(
        [
            '../images/oas1/OAS1_0001_MR1_62_ccseg.tif',
            '../images/oas1/OAS1_0001_MR1_63_ccseg.tif',
            '../images/oas1/OAS1_0001_MR1_64_ccseg.tif',
            '../images/oas1/OAS1_0001_MR1_65_ccseg.tif',
            '../images/oas1/OAS1_0001_MR1_66_ccseg.tif',
            '../images/oas1/OAS1_0001_MR1_67_ccseg.tif',
            '../images/oas1/OAS1_0001_MR1_68_ccseg.tif',
            '../images/oas1/OAS1_0001_MR1_69_ccseg.tif',
            '../images/oas1/OAS1_0001_MR1_70_ccseg.tif',
        ],
        '../input/OAS1_0001_ccseg_opt_1.dat',
        256,
        lambda: 1
    )


def example_oas_1_random_seed():
    main(
        [
            '../images/oas1/OAS1_0001_MR1_62_ccseg.tif',
            '../images/oas1/OAS1_0001_MR1_63_ccseg.tif',
            '../images/oas1/OAS1_0001_MR1_64_ccseg.tif',
            '../images/oas1/OAS1_0001_MR1_65_ccseg.tif',
            '../images/oas1/OAS1_0001_MR1_66_ccseg.tif',
            '../images/oas1/OAS1_0001_MR1_67_ccseg.tif',
            '../images/oas1/OAS1_0001_MR1_68_ccseg.tif',
            '../images/oas1/OAS1_0001_MR1_69_ccseg.tif',
            '../images/oas1/OAS1_0001_MR1_70_ccseg.tif',
        ],
        '../input/OAS1_0001_ccseg_opt_2.dat',
        256,
        lambda: random.randint(1, 10000)
    )


def example_oas_2():
    main(
        [
            '../images/oas2/OAS1_0002_MR1_61_ccseg.tif',
            '../images/oas2/OAS1_0002_MR1_62_ccseg.tif',
            '../images/oas2/OAS1_0002_MR1_63_ccseg.tif',
            '../images/oas2/OAS1_0002_MR1_64_ccseg.tif',
            '../images/oas2/OAS1_0002_MR1_65_ccseg.tif',
            '../images/oas2/OAS1_0002_MR1_66_ccseg.tif',
            '../images/oas2/OAS1_0002_MR1_67_ccseg.tif',
            '../images/oas2/OAS1_0002_MR1_68_ccseg.tif',
        ],
        '../input/OAS1_0002_ccseg_opt_1.dat',
        256,
        lambda: 1
    )


def example_oas_2_random_seed():
    main(
        [
            '../images/oas2/OAS1_0002_MR1_61_ccseg.tif',
            '../images/oas2/OAS1_0002_MR1_62_ccseg.tif',
            '../images/oas2/OAS1_0002_MR1_63_ccseg.tif',
            '../images/oas2/OAS1_0002_MR1_64_ccseg.tif',
            '../images/oas2/OAS1_0002_MR1_65_ccseg.tif',
            '../images/oas2/OAS1_0002_MR1_66_ccseg.tif',
            '../images/oas2/OAS1_0002_MR1_67_ccseg.tif',
            '../images/oas2/OAS1_0002_MR1_68_ccseg.tif',
        ],
        '../input/OAS1_0002_ccseg_opt_2.dat',
        256,
        lambda: random.randint(1, 10000)
    )


if __name__ == "__main__":
    pass
