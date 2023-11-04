import numpy as np

import tif_builder


def main(input_path: str, output_path: str, xy_size: int, include_zero: bool):
    values = np.loadtxt(input_path, dtype=int)
    tif_builder.build(values, xy_size, xy_size, include_zero, output_path)


def example_bunny_le_0():
    main(
        '../input/objs_bunny_sanitised.txt',
        '../images/bunny_le_0',
        512,
        True
    )


def example_bunny_le_1():
    main(
        '../input/objs_bunny_sanitised.txt',
        '../images/bunny_le_1',
        512,
        False
    )


def example_bunny_be_0():
    main(
        '../input/objs_bunny_sanitised_be.txt',
        '../images/bunny_be_0',
        512,
        True
    )


def example_bunny_be_1():
    main(
        '../input/objs_bunny_sanitised_be.txt',
        '../images/bunny_be_1',
        512,
        False
    )


if __name__ == "__main__":
    pass
