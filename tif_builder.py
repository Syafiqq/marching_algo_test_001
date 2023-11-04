from pathlib import Path
import numpy as np
import cv2
import os


def build(values: [int], x_size: int, y_size: int, include_zero: bool, path: str):
    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)
    z_size = int(len(values) / y_size / x_size)

    values = np.reshape(values, (z_size, y_size, x_size))
    values = np.flip(values, (0, 1))

    # find max and min
    masked = np.ma.masked_equal(values, 0.0, copy=False)
    v_min = masked.min()
    v_max = masked.max()

    # normalize to 0 - 255
    if not include_zero and v_min != v_max:
        values = values - v_min
        values[values < 0] = 0
    values = values / v_max * 255

    for i in range(z_size):
        im = np.array(values[i], dtype=np.uint8)
        gray_img = cv2.cvtColor(im, cv2.COLOR_GRAY2BGR)
        cv2.imwrite(str(path / f'{i}.tif'), gray_img)


if __name__ == "__main__":
    pass
