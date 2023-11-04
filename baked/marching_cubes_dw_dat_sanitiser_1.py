import numpy as np

import dat_loader


def main(input_path: str, output_path: str, little_endian: bool):
    data, dimension = dat_loader.load_v1(input_path, 0, little_endian=little_endian)
    np.savetxt(output_path, data, fmt='%d')
    print(dimension)


def example_sq_object():
    main(
        '../input/sq_object.dat',
        '../input/sq_object_sanitised.txt',
        True
    )


def example_stagbettle_208x208x123():
    main(
        '../input/stagbeetle208x208x123.dat',
        '../input/stagbeetle208x208x123_sanitised.txt',
        True
    )


def example_stagbettle_832x832x494():
    main(
        '../input/stagbeetle832x832x494.dat',
        '../input/stagbeetle832x832x494_sanitised.txt',
        True
    )


def example_stagbettle_277x277x164():
    main(
        '../input/stagbeetle277x277x164.dat',
        '../input/stagbeetle277x277x164_sanitised.txt',
        True
    )


def example_stagbettle_416x416x247():
    main(
        '../input/stagbeetle416x416x247.dat',
        '../input/stagbeetle416x416x247_sanitised.txt',
        True
    )


if __name__ == "__main__":
    pass
