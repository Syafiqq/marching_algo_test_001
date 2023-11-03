import struct
import csv


def load(filename: str, output_path: str) -> None:
    with open(filename, "rb") as fp:
        size_x, size_y, size_z = struct.unpack("<HHH", fp.read(6))
        data = [[[0 for _ in range(size_x)] for _ in range(size_y)] for _ in range(size_z)]

        for z in range(size_z):
            for y in range(size_y):
                for x in range(size_x):
                    data[z][y][x] = struct.unpack("<H", fp.read(2))[0]

        with open(output_path, 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)

            for data_z in data:
                writer.writerows(data_z)
                writer.writerow([])


def main(input_path, output_path):
    load(input_path, output_path)


def example_load_stag_beetle():
    main(
        '../objs/stagbeetle208x208x123.dat',
        '/tmp/stagbeetle208x208x123.csv'
    )


if __name__ == "__main__":
    pass
