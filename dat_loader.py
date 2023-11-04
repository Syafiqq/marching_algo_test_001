import struct


def load_v1(
        input_path: str,
        iso_value: int,
        little_endian: bool
) -> ([int], (int, int, int)):
    endian = "<" if little_endian else ">"
    with open(input_path, "rb") as fp:
        size_x, size_y, size_z = struct.unpack("<HHH", fp.read(6))
        data = [0 for _ in range(size_x * size_y * size_z)]

        i = 0
        if iso_value >= 0:
            for z in range(size_z):
                for y in range(size_y):
                    for x in range(size_x):
                        if struct.unpack(f'{endian}H', fp.read(2))[0] > iso_value:
                            data[i] = 1
                        i += 1
        else:
            for z in range(size_z):
                for y in range(size_y):
                    for x in range(size_x):
                        data[i] = struct.unpack(f'{endian}H', fp.read(2))[0]
                        i += 1

    return data, (size_x, size_y, size_z)


def load_v2(
        input_path: str,
        size_xy: int,
        size_z: int,
        iso_value: int,
        little_endian: bool
) -> ([int], (int, int, int)):
    endian = "<" if little_endian else ">"
    with open(input_path, "rb") as fp:
        data = [0 for _ in range(size_xy * size_xy * size_z)]

        i = 0
        if iso_value >= 0:
            for z in range(size_z):
                for y in range(size_xy):
                    for x in range(size_xy):
                        if struct.unpack(f'{endian}H', fp.read(2))[0] > iso_value:
                            data[i] = 1
                        i += 1
        else:
            for z in range(size_z):
                for y in range(size_xy):
                    for x in range(size_xy):
                        data[i] = struct.unpack(f'{endian}H', fp.read(2))[0]
                        i += 1

    return data, (size_xy, size_xy, size_z)


def load_v3(
        input_paths: str,
        size_xy: int,
        iso_value: int,
        little_endian: bool
) -> ([int], (int, int, int)):
    endian = "<" if little_endian else ">"
    data = [0 for _ in range(size_xy * size_xy * len(input_paths))]
    i = 0
    for input_path in input_paths:
        with open(input_path, "rb") as fp:
            if iso_value >= 0:
                for y in range(size_xy):
                    for x in range(size_xy):
                        if struct.unpack(f'{endian}H', fp.read(2))[0] > iso_value:
                            data[i] = 1
                        i += 1
            else:
                for y in range(size_xy):
                    for x in range(size_xy):
                        data[i] = struct.unpack(f'{endian}H', fp.read(2))[0]
                        i += 1

    return data, (size_xy, size_xy, len(input_paths))
