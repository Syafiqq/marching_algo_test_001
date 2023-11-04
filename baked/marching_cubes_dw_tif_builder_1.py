import numpy as np

import tif_builder


def main(input_path: str, output_path: str, xy_size: int, include_zero: bool):
    values = np.loadtxt(input_path, dtype=int)
    tif_builder.build(values, xy_size, xy_size, include_zero, output_path)


if __name__ == "__main__":
    pass
