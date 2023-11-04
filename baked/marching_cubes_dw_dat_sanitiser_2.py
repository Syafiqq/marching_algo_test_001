import numpy as np

import dat_loader


def main(input_paths: [str], output_path: str, size_xy: int, iso_value: int, little_endian: bool):
    data, dimension = dat_loader.load_v3(input_paths, size_xy, iso_value, little_endian=little_endian)
    np.savetxt(output_path, data, fmt='%d')
    print(dimension)


if __name__ == "__main__":
    pass
