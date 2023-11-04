import numpy as np

import dat_loader


def main(input_path: str, output_path: str, little_endian: bool):
    data, dimension = dat_loader.load_v1(input_path, 0, little_endian=little_endian)
    np.savetxt(output_path, data, fmt='%d')
    print(dimension)


if __name__ == "__main__":
    pass
