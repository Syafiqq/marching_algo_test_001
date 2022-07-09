def __mid_point(p1, p2):
    pt = abs(p1 - p2) / 2
    return p1 + pt


def to_points(points, point_type):
    if point_type == 0:
        # 0 0 0 0 0 0 0 0 ~ 0
        #
        #   6     7
        # 4     5
        #   2     3
        # 0     1
        #
        #                   .  .  .
        #                   .  .  .
        #                   .  .  .
        #          .  .  .
        #          .  .  .
        #          .  .  .
        # .  .  .
        # .  .  .
        # .  .  .
        #
        return []

    elif point_type == 0b10000000:
        # 1 0 0 0 0 0 0 0 ~ 128
        #
        #   6     7
        # 4     5
        #   2     3
        # o     1
        #
        #                   .  .  .
        #                   .  .  .
        #                   .  .  .
        #          .  .  .
        #          .  .  .
        #          1  .  .
        # .  .  .
        # 2  .  .
        # .  0  .
        #
        p0 = __mid_point(points[0], points[1])
        p1 = __mid_point(points[0], points[2])
        p2 = __mid_point(points[0], points[4])

        return [p0, p1, p2]

    elif point_type == 0b01000000:
        # 0 1 0 0 0 0 0 0
        #
        #   6     7
        # 4     5
        #   2     3
        # 0     o
        #
        #                   .  .  .
        #                   .  .  .
        #                   .  .  .
        #          .  .  .
        #          .  .  .
        #          .  .  1
        # .  .  .
        # .  .  2
        # .  0  .
        #
        p0 = __mid_point(points[0], points[1])
        p1 = __mid_point(points[1], points[3])
        p2 = __mid_point(points[1], points[5])

        return [p0, p1, p2]

    elif point_type == 0b00100000:
        # 0 0 1 0 0 0 0 0
        #
        #   6     7
        # 4     5
        #   o     3
        # 0     1
        #
        #                   .  .  .
        #                   2  .  .
        #                   .  1  .
        #          .  .  .
        #          .  .  .
        #          0  .  .
        # .  .  .
        # .  .  .
        # .  .  .
        #
        p0 = __mid_point(points[0], points[2])
        p1 = __mid_point(points[2], points[3])
        p2 = __mid_point(points[2], points[6])

        return [p0, p1, p2]

    elif point_type == 0b00010000:
        # 0 0 0 1 0 0 0 0
        #
        #   6     7
        # 4     5
        #   2     o
        # 0     1
        #
        #                   .  .  .
        #                   .  .  2
        #                   .  1  .
        #          .  .  .
        #          .  .  .
        #          .  .  0
        # .  .  .
        # .  .  .
        # .  .  .
        #
        p0 = __mid_point(points[1], points[3])
        p1 = __mid_point(points[2], points[3])
        p2 = __mid_point(points[3], points[7])

        return [p0, p1, p2]

    elif point_type == 0b00001000:
        # 0 0 0 0 1 0 0 0
        #
        #   6     7
        # o     5
        #   2     3
        # 0     1
        #
        #                   .  .  .
        #                   .  .  .
        #                   .  .  .
        #          2  .  .
        #          .  .  .
        #          .  .  .
        # .  1  .
        # 0  .  .
        # .  .  .
        #
        p0 = __mid_point(points[0], points[4])
        p1 = __mid_point(points[4], points[5])
        p2 = __mid_point(points[4], points[6])

        return [p0, p1, p2]

    elif point_type == 0b00000100:
        # 0 0 0 0 0 1 0 0
        #
        #   6     7
        # 4     o
        #   2     3
        # 0     1
        #
        #                   .  .  .
        #                   .  .  .
        #                   .  .  .
        #          .  .  2
        #          .  .  .
        #          .  .  .
        # .  1  .
        # .  .  0
        # .  .  .
        #
        p0 = __mid_point(points[1], points[5])
        p1 = __mid_point(points[4], points[5])
        p2 = __mid_point(points[5], points[7])

        return [p0, p1, p2]

    elif point_type == 0b00000010:
        # 0 0 0 0 0 0 1 0
        #
        #   o     7
        # 4     5
        #   2     3
        # 0     1
        #
        #                   .  2  .
        #                   0  .  .
        #                   .  .  .
        #          1  .  .
        #          .  .  .
        #          .  .  .
        # .  .  .
        # .  .  .
        # .  .  .
        #
        p0 = __mid_point(points[2], points[6])
        p1 = __mid_point(points[4], points[6])
        p2 = __mid_point(points[6], points[7])

        return [p0, p1, p2]

    elif point_type == 0b00000001:
        # 0 0 0 0 0 0 0 1
        #
        #   6     o
        # 4     5
        #   2     3
        # 0     1
        #
        #                   .  2  .
        #                   .  .  .
        #                   .  .  .
        #          .  .  1
        #          .  .  0
        #          .  .  .
        # .  .  .
        # .  .  .
        # .  .  .
        #
        p0 = __mid_point(points[3], points[7])
        p1 = __mid_point(points[5], points[7])
        p2 = __mid_point(points[6], points[7])

        return [p0, p1, p2]

    elif point_type == 0b11000000:
        # 1 1 0 0 0 0 0 0
        #
        #   6     7
        # 4     5
        #   2     3
        # o     o
        #
        #                   .  .  .
        #                   .  .  .
        #                   .  .  .
        #          .  .  .
        #          .  .  .
        #          0  .  1
        # .  .  .
        # 2  .  3
        # .  .  .
        #
        p0 = __mid_point(points[0], points[2])
        p1 = __mid_point(points[1], points[3])
        p2 = __mid_point(points[0], points[4])
        p3 = __mid_point(points[1], points[5])

        return [p0, p1, p2, p3]

    elif point_type == 0b10100000:
        # 1 0 1 0 0 0 0 0
        #
        #   6     7
        # 4     5
        #   o     3
        # o     1
        #
        #                   .  .  .
        #                   3  .  .
        #                   .  1  .
        #          .  .  .
        #          .  .  .
        #          .  .  .
        # .  .  .
        # 2  .  .
        # .  0  .
        #
        p0 = __mid_point(points[0], points[1])
        p1 = __mid_point(points[2], points[3])
        p2 = __mid_point(points[0], points[4])
        p3 = __mid_point(points[2], points[6])

        return [p0, p1, p2, p3]

    elif point_type == 0b01100000:
        # 0 1 1 0 0 0 0 0
        #
        #   6     7
        # 4     5
        #   o     3
        # 0     o
        #
        #                   .  .  .
        #                   5  .  .
        #                   .  3  .
        #          .  .  .
        #          .  .  .
        #          1  .  2
        # .  .  .
        # .  .  4
        # .  0  .
        #
        p0 = __mid_point(points[0], points[1])
        p1 = __mid_point(points[0], points[2])
        p2 = __mid_point(points[1], points[3])
        p3 = __mid_point(points[2], points[3])
        p4 = __mid_point(points[1], points[5])
        p5 = __mid_point(points[2], points[6])

        return [p0, p1, p2, p3, p4, p5]

    elif point_type == 0b10010000:
        # 1 0 0 1 0 0 0 0
        #
        #   6     7
        # 4     5
        #   2     o
        # o     1
        #
        #                   .  .  .
        #                   .  .  5
        #                   .  3  .
        #          .  .  .
        #          .  .  .
        #          1  .  2
        # .  .  .
        # 4  .  .
        # .  0  .
        #
        p0 = __mid_point(points[0], points[1])
        p1 = __mid_point(points[0], points[2])
        p2 = __mid_point(points[1], points[3])
        p3 = __mid_point(points[2], points[3])
        p4 = __mid_point(points[0], points[4])
        p5 = __mid_point(points[3], points[7])

        return [p0, p1, p2, p3, p4, p5]

    elif point_type == 0b01010000:
        # 0 1 0 1 0 0 0 0
        #
        #   6     7
        # 4     5
        #   2     o
        # 0     o
        #
        #                   .  .  .
        #                   .  .  3
        #                   .  1  .
        #          .  .  .
        #          .  .  .
        #          .  .  .
        # .  .  .
        # .  .  2
        # .  0  .
        #
        p0 = __mid_point(points[0], points[1])
        p1 = __mid_point(points[2], points[3])
        p2 = __mid_point(points[1], points[5])
        p3 = __mid_point(points[3], points[7])

        return [p0, p1, p2, p3]

    elif point_type == 0b00110000:
        # 0 0 1 1 0 0 0 0
        #
        #   6     7
        # 4     5
        #   o     o
        # 0     1
        #
        #                   .  .  .
        #                   2  .  3
        #                   .  .  .
        #          .  .  .
        #          .  .  .
        #          0  .  1
        # .  .  .
        # .  .  .
        # .  .  .
        #
        p0 = __mid_point(points[0], points[2])
        p1 = __mid_point(points[1], points[3])
        p2 = __mid_point(points[2], points[6])
        p3 = __mid_point(points[3], points[7])

        return [p0, p1, p2, p3]

    elif point_type == 0b10001000:
        # 1 0 0 0 1 0 0 0
        #
        #   6     7
        # o     5
        #   2     3
        # o     1
        #
        #                   .  .  .
        #                   .  .  .
        #                   .  .  .
        #          3  .  .
        #          .  .  .
        #          1  .  .
        # .  2  .
        # .  .  .
        # .  0  .
        #
        p0 = __mid_point(points[0], points[1])
        p1 = __mid_point(points[0], points[2])
        p2 = __mid_point(points[4], points[5])
        p3 = __mid_point(points[4], points[6])

        return [p0, p1, p2, p3]

    elif point_type == 0b01001000:
        # 0 1 0 0 1 0 0 0
        #
        #   6     7
        # o     5
        #   2     3
        # 0     o
        #
        #                   .  .  .
        #                   .  .  .
        #                   .  .  .
        #          5  .  .
        #          .  .  .
        #          .  .  1
        # .  4  .
        # 2  .  3
        # .  0  .
        #
        p0 = __mid_point(points[0], points[1])
        p1 = __mid_point(points[1], points[3])
        p2 = __mid_point(points[0], points[4])
        p3 = __mid_point(points[1], points[5])
        p4 = __mid_point(points[4], points[5])
        p5 = __mid_point(points[4], points[6])

        return [p0, p1, p2, p3, p4, p5]

    elif point_type == 0b00101000:
        # 0 0 1 0 1 0 0 0
        #
        #   6     7
        # o     5
        #   o     3
        # 0     1
        #
        #                   .  .  .
        #                   3  .  .
        #                   .  1  .
        #          5  .  .
        #          .  .  .
        #          0  .  .
        # .  4  .
        # 2  .  .
        # .  .  .
        #
        p0 = __mid_point(points[0], points[2])
        p1 = __mid_point(points[2], points[3])
        p2 = __mid_point(points[0], points[4])
        p3 = __mid_point(points[2], points[6])
        p4 = __mid_point(points[4], points[5])
        p5 = __mid_point(points[4], points[6])

        return [p0, p1, p2, p3, p4, p5]

    elif point_type == 0b00011000:
        # 0 0 0 1 1 0 0 0
        #
        #   6     7
        # o     5
        #   2     o
        # 0     1
        #
        #                   .  .  .
        #                   .  .  3
        #                   .  1  .
        #          5  .  .
        #          .  .  .
        #          .  .  0
        # .  4  .
        # 2  .  .
        # .  .  .
        #
        p0 = __mid_point(points[1], points[3])
        p1 = __mid_point(points[2], points[3])
        p2 = __mid_point(points[0], points[4])
        p3 = __mid_point(points[3], points[7])
        p4 = __mid_point(points[4], points[5])
        p5 = __mid_point(points[4], points[6])

        return [p0, p1, p2, p3, p4, p5]

    elif point_type == 0b10000100:
        # 1 0 0 0 0 1 0 0
        #
        #   6     7
        # 4     o
        #   2     3
        # o     1
        #
        #                   .  .  .
        #                   .  .  .
        #                   .  .  .
        #          .  .  5
        #          .  .  .
        #          1  .  .
        # .  4  .
        # 2  .  3
        # .  0  .
        #
        p0 = __mid_point(points[0], points[1])
        p1 = __mid_point(points[0], points[2])
        p2 = __mid_point(points[0], points[4])
        p3 = __mid_point(points[1], points[5])
        p4 = __mid_point(points[4], points[5])
        p5 = __mid_point(points[5], points[7])

        return [p0, p1, p2, p3, p4, p5]

    elif point_type == 0b01000100:
        # 0 1 0 0 0 1 0 0
        #
        #   6     7
        # 4     o
        #   2     3
        # 0     o
        #
        #                   .  .  .
        #                   .  .  .
        #                   .  .  .
        #          .  .  3
        #          .  .  .
        #          .  .  1
        # .  2  .
        # .  .  .
        # .  0  .
        #
        p0 = __mid_point(points[0], points[1])
        p1 = __mid_point(points[1], points[3])
        p2 = __mid_point(points[4], points[5])
        p3 = __mid_point(points[5], points[7])

        return [p0, p1, p2, p3]

    elif point_type == 0b00100100:
        # 0 0 1 0 0 1 0 0
        #
        #   6     7
        # 4     o
        #   o     3
        # 0     1
        #
        #                   .  .  .
        #                   3  .  .
        #                   .  1  .
        #          .  .  5
        #          .  .  2
        #          0  .  .
        # .  4  .
        # .  .  .
        # .  .  .
        #
        p0 = __mid_point(points[0], points[2])
        p1 = __mid_point(points[2], points[3])
        p2 = __mid_point(points[1], points[5])
        p3 = __mid_point(points[2], points[6])
        p4 = __mid_point(points[4], points[5])
        p5 = __mid_point(points[5], points[7])

        return [p0, p1, p2, p3, p4, p5]

    elif point_type == 0b00010100:
        # 0 0 0 1 0 1 0 0
        #
        #   6     7
        # 4     o
        #   2     o
        # 0     1
        #
        #                   .  .  .
        #                   .  .  3
        #                   .  1  .
        #          .  .  5
        #          .  .  .
        #          .  .  0
        # .  4  .
        # .  .  2
        # .  .  .
        #
        p0 = __mid_point(points[1], points[3])
        p1 = __mid_point(points[2], points[3])
        p2 = __mid_point(points[1], points[5])
        p3 = __mid_point(points[3], points[7])
        p4 = __mid_point(points[4], points[5])
        p5 = __mid_point(points[5], points[7])

        return [p0, p1, p2, p3, p4, p5]

    elif point_type == 0b00001100:
        # 0 0 0 0 1 1 0 0
        #
        #   6     7
        # o     o
        #   2     3
        # 0     1
        #
        #                   .  .  .
        #                   .  .  .
        #                   .  .  .
        #          2  .  3
        #          .  .  .
        #          .  .  .
        # .  .  .
        # 0  .  1
        # .  .  .
        #
        p0 = __mid_point(points[0], points[4])
        p1 = __mid_point(points[1], points[5])
        p2 = __mid_point(points[4], points[6])
        p3 = __mid_point(points[5], points[7])

        return [p0, p1, p2, p3]

    elif point_type == 0b10000010:
        # 1 0 0 0 0 0 1 0
        #
        #   o     7
        # 4     5
        #   2     3
        # o     1
        #
        #                   .  5  .
        #                   3  .  .
        #                   .  .  .
        #          4  .  .
        #          1  .  .
        #          .  .  .
        # .  .  .
        # 2  .  .
        # .  0  .
        #
        p0 = __mid_point(points[0], points[1])
        p1 = __mid_point(points[0], points[2])
        p2 = __mid_point(points[0], points[4])
        p3 = __mid_point(points[2], points[6])
        p4 = __mid_point(points[4], points[6])
        p5 = __mid_point(points[6], points[7])

        return [p0, p1, p2, p3, p4, p5]

    elif point_type == 0b01000010:
        # 0 1 0 0 0 0 1 0
        #
        #   o     7
        # 4     5
        #   2     3
        # 0     o
        #
        #                   .  5  .
        #                   3  .  .
        #                   .  .  .
        #          4  .  .
        #          .  .  .
        #          .  .  1
        # .  .  .
        # .  .  2
        # .  0  .
        #
        p0 = __mid_point(points[0], points[1])
        p1 = __mid_point(points[1], points[3])
        p2 = __mid_point(points[1], points[5])
        p3 = __mid_point(points[2], points[6])
        p4 = __mid_point(points[4], points[6])
        p5 = __mid_point(points[6], points[7])

        return [p0, p1, p2, p3, p4, p5]

    elif point_type == 0b00100010:
        # 0 0 1 0 0 0 1 0
        #
        #   o     7
        # 4     5
        #   o      3
        # 0     1
        #
        #                   .  3  .
        #                   .  .  .
        #                   .  1  .
        #          2  .  .
        #          .  .  .
        #          0  .  .
        # .  .  .
        # .  .  .
        # .  .  .
        #
        p0 = __mid_point(points[0], points[2])
        p1 = __mid_point(points[2], points[3])
        p2 = __mid_point(points[4], points[6])
        p3 = __mid_point(points[6], points[7])

        return [p0, p1, p2, p3]

    elif point_type == 0b00010010:
        # 0 0 0 1 0 0 1 0
        #
        #   o     7
        # 4     5
        #   2     o
        # 0     1
        #
        #                   .  5  .
        #                   2  .  3
        #                   .  1  .
        #          4  .  .
        #          .  .  .
        #          .  .  0
        # .  .  .
        # .  .  .
        # .  .  .
        #
        p0 = __mid_point(points[1], points[3])
        p1 = __mid_point(points[2], points[3])
        p2 = __mid_point(points[2], points[6])
        p3 = __mid_point(points[3], points[7])
        p4 = __mid_point(points[4], points[6])
        p5 = __mid_point(points[6], points[7])

        return [p0, p1, p2, p3, p4, p5]

    elif point_type == 0b00001010:
        # 0 0 0 0 1 0 1 0
        #
        #   o     7
        # o     5
        #   2     3
        # 0     1
        #
        #                   .  3  .
        #                   1  .  .
        #                   .  .  .
        #          .  2  .
        #          0  .  .
        #          .  .  .
        # .  .  .
        # .  .  .
        # .  .  .
        #
        p0 = __mid_point(points[0], points[4])
        p1 = __mid_point(points[2], points[6])
        p2 = __mid_point(points[4], points[5])
        p3 = __mid_point(points[6], points[7])

        return [p0, p1, p2, p3]

    elif point_type == 0b00000110:
        # 0 0 0 0 0 1 1 0
        #
        #   o     7
        # 4     o
        #   2     3
        # 0     1
        #
        #                   .  5  .
        #                   1  .  .
        #                   .  .  .
        #          3  .  4
        #          .  .  .
        #          .  .  .
        # .  2  .
        # .  .  0
        # .  .  .
        #
        p0 = __mid_point(points[1], points[5])
        p1 = __mid_point(points[2], points[6])
        p2 = __mid_point(points[4], points[5])
        p3 = __mid_point(points[4], points[6])
        p4 = __mid_point(points[5], points[7])
        p5 = __mid_point(points[6], points[7])

        return [p0, p1, p2, p3, p4, p5]

    elif point_type == 0b10000001:
        # 1 0 0 0 0 0 0 1
        #
        #   6     o
        # 4     5
        #   2     3
        # o     1
        #
        #                   .  5  .
        #                   .  .  3
        #                   .  .  .
        #          .  .  4
        #          .  .  .
        #          1  .  .
        # .  .  .
        # 2  .  .
        # .  0  .
        #
        p0 = __mid_point(points[0], points[1])
        p1 = __mid_point(points[0], points[2])
        p2 = __mid_point(points[0], points[4])
        p3 = __mid_point(points[3], points[7])
        p4 = __mid_point(points[5], points[7])
        p5 = __mid_point(points[6], points[7])

        return [p0, p1, p2, p3, p4, p5]

    elif point_type == 0b01000001:
        # 0 1 0 0 0 0 0 1
        #
        #   6     o
        # 4     5
        #   2     3
        # 0     o
        #
        #                   .  5  .
        #                   .  .  3
        #                   .  .  .
        #          .  .  4
        #          .  .  .
        #          .  .  1
        # .  .  .
        # .  .  2
        # .  0  .
        #
        p0 = __mid_point(points[0], points[1])
        p1 = __mid_point(points[1], points[3])
        p2 = __mid_point(points[1], points[5])
        p3 = __mid_point(points[3], points[7])
        p4 = __mid_point(points[5], points[7])
        p5 = __mid_point(points[6], points[7])

        return [p0, p1, p2, p3, p4, p5]

    elif point_type == 0b00100001:
        # 0 0 1 0 0 0 0 1
        #
        #   6     o
        # 4     5
        #   o     3
        # 0     1
        #
        #                   .  5  .
        #                   2  .  3
        #                   .  1  .
        #          .  .  4
        #          .  .  .
        #          0  .  .
        # .  .  .
        # .  .  .
        # .  .  .
        #
        p0 = __mid_point(points[0], points[2])
        p1 = __mid_point(points[2], points[3])
        p2 = __mid_point(points[2], points[6])
        p3 = __mid_point(points[3], points[7])
        p4 = __mid_point(points[5], points[7])
        p5 = __mid_point(points[6], points[7])

        return [p0, p1, p2, p3, p4, p5]

    elif point_type == 0b00010001:
        # 0 0 0 0 0 0 0 1
        #
        #   6     o
        # 4     5
        #   2     o
        # 0     1
        #
        #                   .  3  .
        #                   .  .  .
        #                   .  1  .
        #          .  .  2
        #          .  .  .
        #          .  .  0
        # .  .  .
        # .  .  .
        # .  .  .
        #
        p0 = __mid_point(points[1], points[3])
        p1 = __mid_point(points[2], points[3])
        p2 = __mid_point(points[5], points[7])
        p3 = __mid_point(points[6], points[7])

        return [p0, p1, p2, p3]

    elif point_type == 0b00001001:
        # 0 0 0 0 1 0 0 1
        #
        #   6     o
        # o     5
        #   2     3
        # 0     1
        #
        #                   .  5  .
        #                   .  .  1
        #                   .  .  .
        #          3  .  4
        #          .  .  .
        #          .  .  .
        # .  2  .
        # 0  .  .
        # .  .  .
        #
        p0 = __mid_point(points[0], points[4])
        p1 = __mid_point(points[3], points[7])
        p2 = __mid_point(points[4], points[5])
        p3 = __mid_point(points[4], points[6])
        p4 = __mid_point(points[5], points[7])
        p5 = __mid_point(points[6], points[7])

        return [p0, p1, p2, p3, p4, p5]

    elif point_type == 0b00000101:
        # 0 0 0 0 0 1 0 1
        #
        #   6     o
        # 4     o
        #   2     3
        # 0     1
        #
        #                   .  3  .
        #                   .  .  1
        #                   .  .  .
        #          .  .  .
        #          .  .  .
        #          .  .  .
        # .  2  .
        # .  .  0
        # .  .  .
        #
        p0 = __mid_point(points[1], points[5])
        p1 = __mid_point(points[3], points[7])
        p2 = __mid_point(points[4], points[5])
        p3 = __mid_point(points[6], points[7])

        return [p0, p1, p2, p3]

    elif point_type == 0b00000011:
        # 0 0 0 0 0 0 1 1
        #
        #   o     o
        # 4     5
        #   2     3
        # 0     1
        #
        #                   .  .  .
        #                   0  .  1
        #                   .  .  .
        #          2  .  3
        #          .  .  .
        #          .  .  .
        # .  .  .
        # .  .  .
        # .  .  .
        #
        p0 = __mid_point(points[2], points[6])
        p1 = __mid_point(points[3], points[7])
        p2 = __mid_point(points[4], points[6])
        p3 = __mid_point(points[5], points[7])

        return [p0, p1, p2, p3]

    elif point_type == 0b11100000:
        # 1 1 1 0 0 0 0 0
        #
        #   6     7
        # 4      5
        #   o     3
        # o     o
        #
        #                   .  .  .
        #                   4  .  .
        #                   .  1  .
        #          .  .  .
        #          .  .  .
        #          .  .  0
        # .  .  .
        # 2  .  3
        # .  .  .
        #
        p0 = __mid_point(points[1], points[3])
        p1 = __mid_point(points[2], points[3])
        p2 = __mid_point(points[0], points[4])
        p3 = __mid_point(points[1], points[5])
        p4 = __mid_point(points[2], points[6])

        return [p0, p1, p2, p3, p4]

    elif point_type == 0b11010000:
        # 1 1 0 1 0 0 0 0
        #
        #   6     7
        # 4     5
        #   2     o
        # o     o
        #
        #                   .  .  .
        #                   .  .  4
        #                   .  1  .
        #          .  .  .
        #          .  .  .
        #          0  .  .
        # .  .  .
        # 2  .  3
        # .  .  .
        #
        p0 = __mid_point(points[0], points[2])
        p1 = __mid_point(points[2], points[3])
        p2 = __mid_point(points[0], points[4])
        p3 = __mid_point(points[1], points[5])
        p4 = __mid_point(points[3], points[7])

        return [p0, p1, p2, p3, p4]

    elif point_type == 0b10110000:
        # 1 0 1 1 0 0 0 0
        #
        #   6     7
        # 4     5
        #   o     o
        # o     1
        #
        #                   .  .  .
        #                   3  .  4
        #                   .  .  .
        #          .  .  .
        #          .  .  .
        #          .  .  1
        # .  .  .
        # 2  .  .
        # .  0  .
        #
        p0 = __mid_point(points[0], points[1])
        p1 = __mid_point(points[1], points[3])
        p2 = __mid_point(points[0], points[4])
        p3 = __mid_point(points[2], points[6])
        p4 = __mid_point(points[3], points[7])

        return [p0, p1, p2, p3, p4]

    elif point_type == 0b01110000:
        # 0 1 1 1 0 0 0 0
        #
        #   6     7
        # 4     5
        #   o     o
        # 0     o
        #
        #                   .  .  .
        #                   3  .  4
        #                   .  .  .
        #          .  .  .
        #          .  .  .
        #          1  .  .
        # .  .  .
        # .  .  2
        # .  0  .
        #
        p0 = __mid_point(points[0], points[1])
        p1 = __mid_point(points[0], points[2])
        p2 = __mid_point(points[1], points[5])
        p3 = __mid_point(points[2], points[6])
        p4 = __mid_point(points[3], points[7])

        return [p0, p1, p2, p3, p4]

    elif point_type == 0b11001000:
        # 1 1 0 0 1 0 0 0
        #
        #   6     7
        # o     5
        #   2     3
        # o     o
        #
        #                   .  .  .
        #                   .  .  .
        #                   .  .  .
        #          4  .  .
        #          .  .  .
        #          0  .  1
        # .  3  .
        # .  .  2
        # .  .  .
        #
        p0 = __mid_point(points[0], points[2])
        p1 = __mid_point(points[1], points[3])
        p2 = __mid_point(points[1], points[5])
        p3 = __mid_point(points[4], points[5])
        p4 = __mid_point(points[4], points[6])

        return [p0, p1, p2, p3, p4]

    elif point_type == 0b10101000:
        # 1 0 1 0 1 0 0 0
        #
        #   6     7
        # o     5
        #   o     3
        # o     1
        #
        #                   .  .  .
        #                   .  .  .
        #                   .  .  .
        #          .  .  .
        #          .  .  .
        #          .  .  .
        # .  .  .
        # .  .  .
        # .  .  .
        #
        p0 = __mid_point(points[0], points[1])
        p1 = __mid_point(points[2], points[3])
        p2 = __mid_point(points[2], points[6])
        p3 = __mid_point(points[4], points[5])
        p4 = __mid_point(points[4], points[6])

        return [p0, p1, p2, p3, p4]

    elif point_type == 0b01101000:
        # 0 1 1 0 1 0 0 0
        #
        #   6     7
        # o     5
        #   o     3
        # 0     o
        #
        #                   .  .  .
        #                   6  .  .
        #                   .  3  .
        #          8  .  .
        #          .  .  .
        #          1  .  2
        # .  7  .
        # 4  .  5
        # .  0  .
        #
        p0 = __mid_point(points[0], points[1])
        p1 = __mid_point(points[0], points[2])
        p2 = __mid_point(points[1], points[3])
        p3 = __mid_point(points[2], points[3])
        p4 = __mid_point(points[0], points[4])
        p5 = __mid_point(points[1], points[5])
        p6 = __mid_point(points[2], points[6])
        p7 = __mid_point(points[4], points[5])
        p8 = __mid_point(points[4], points[6])

        return [p0, p1, p2, p3, p4, p5, p6, p7, p8]

    elif point_type == 0b10011000:
        # 1 0 0 1 1 0 0 0
        #
        #   6     7
        # o     5
        #   2     o
        # o     1
        #
        #                   .  .  .
        #                   .  .  4
        #                   .  3  .
        #          .  .  .
        #          6  .  .
        #          1  .  2
        # .  5  .
        # .  .  .
        # .  0  .
        #
        p0 = __mid_point(points[0], points[1])
        p1 = __mid_point(points[0], points[2])
        p2 = __mid_point(points[1], points[3])
        p3 = __mid_point(points[2], points[3])
        p4 = __mid_point(points[3], points[7])
        p5 = __mid_point(points[4], points[5])
        p6 = __mid_point(points[4], points[6])

        return [p0, p1, p2, p3, p4, p5, p6]

    elif point_type == 0b01011000:
        # 0 1 0 1 1 0 0 0
        #
        #   6     7
        # o     5
        #   2     o
        # 0     o
        #
        #                   .  .  .
        #                   .  .  5
        #                   .  1  .
        #          6  .  .
        #          .  .  .
        #          .  .  .
        # .  4  .
        # 2  .  3
        # .  0  .
        #
        p0 = __mid_point(points[0], points[1])
        p1 = __mid_point(points[2], points[3])
        p2 = __mid_point(points[0], points[4])
        p3 = __mid_point(points[1], points[5])
        p4 = __mid_point(points[4], points[5])
        p5 = __mid_point(points[3], points[7])
        p6 = __mid_point(points[4], points[6])

        return [p0, p1, p2, p3, p4, p5, p6]

    elif point_type == 0b00111000:
        # 0 0 1 1 1 0 0 0
        #
        #   6     7
        # o     5
        #   o     o
        # 0     1
        #
        #                   .  .  .
        #                   3  .  4
        #                   .  .  .
        #          6  .  .
        #          .  .  .
        #          0  .  1
        # .  5  .
        # 2  .  .
        # .  .  .
        #
        p0 = __mid_point(points[0], points[2])
        p1 = __mid_point(points[1], points[3])
        p2 = __mid_point(points[0], points[4])
        p3 = __mid_point(points[2], points[6])
        p4 = __mid_point(points[3], points[7])
        p5 = __mid_point(points[4], points[5])
        p6 = __mid_point(points[4], points[6])

        return [p0, p1, p2, p3, p4, p5, p6]

    elif point_type == 0b11000100:
        # 1 1 0 0 0 1 0 0
        #
        #   6     7
        # 4     o
        #   2     3
        # o     o
        #
        #                   .  .  .
        #                   .  .  .
        #                   .  .  .
        #          .  .  4
        #          .  .  .
        #          0  .  1
        # .  3  .
        # 2  .  .
        # .  .  .
        #
        p0 = __mid_point(points[0], points[2])
        p1 = __mid_point(points[1], points[3])
        p2 = __mid_point(points[0], points[4])
        p3 = __mid_point(points[4], points[5])
        p4 = __mid_point(points[5], points[7])

        return [p0, p1, p2, p3, p4]

    elif point_type == 0b10100100:
        # 1 0 1 0 0 1 0 0
        #
        #   6     7
        # 4     o
        #   o     3
        # o     1
        #
        #                   .  .  .
        #                   4  .  .
        #                   .  1  .
        #          .  .  6
        #          .  .  3
        #          .  .  .
        # .  5  .
        # 2  .  .
        # .  0  .
        #
        p0 = __mid_point(points[0], points[1])
        p1 = __mid_point(points[2], points[3])
        p2 = __mid_point(points[0], points[4])
        p3 = __mid_point(points[1], points[5])
        p4 = __mid_point(points[2], points[6])
        p5 = __mid_point(points[4], points[5])
        p6 = __mid_point(points[5], points[7])

        return [p0, p1, p2, p3, p4, p5, p6]

    elif point_type == 0b01100100:
        # 0 1 1 0 0 1 0 0
        #
        #   6     7
        # 4     o
        #   o     3
        # 0     o
        #
        #                   .  6  .
        #                   2  .  .
        #                   .  .  .
        #          4  .  5
        #          .  .  .
        #          .  .  1
        # .  3  .
        # .  .  .
        # .  0  .
        #
        p0 = __mid_point(points[0], points[1])
        p1 = __mid_point(points[1], points[3])
        p2 = __mid_point(points[2], points[6])
        p3 = __mid_point(points[4], points[5])
        p4 = __mid_point(points[4], points[6])
        p5 = __mid_point(points[5], points[7])
        p6 = __mid_point(points[6], points[7])

        return [p0, p1, p2, p3, p4, p5, p6]

    elif point_type == 0b10010100:
        pass

    elif point_type == 0b01010100:
        pass

    elif point_type == 0b00110100:
        pass

    elif point_type == 0b10001100:
        pass

    elif point_type == 0b01001100:
        pass

    elif point_type == 0b00101100:
        pass

    elif point_type == 0b00011100:
        pass

    elif point_type == 0b11000010:
        pass

    elif point_type == 0b10100010:
        pass

    elif point_type == 0b01100010:
        pass

    elif point_type == 0b10010010:
        pass

    elif point_type == 0b01010010:
        pass

    elif point_type == 0b00110010:
        pass

    elif point_type == 0b10001010:
        pass

    elif point_type == 0b01001010:
        pass

    elif point_type == 0b00101010:
        pass

    elif point_type == 0b00011010:
        pass

    elif point_type == 0b10000110:
        pass

    elif point_type == 0b01000110:
        pass

    elif point_type == 0b00100110:
        pass

    elif point_type == 0b00010110:
        pass

    elif point_type == 0b00001110:
        pass

    elif point_type == 0b11000001:
        pass

    elif point_type == 0b10100001:
        pass

    elif point_type == 0b01100001:
        pass

    elif point_type == 0b10010001:
        pass

    elif point_type == 0b01010001:
        pass

    elif point_type == 0b00110001:
        pass

    elif point_type == 0b10001001:
        pass

    elif point_type == 0b01001001:
        pass

    elif point_type == 0b00101001:
        pass

    elif point_type == 0b00011001:
        pass

    elif point_type == 0b10000101:
        pass

    elif point_type == 0b01000101:
        pass

    elif point_type == 0b00100101:
        pass

    elif point_type == 0b00010101:
        pass

    elif point_type == 0b00001101:
        pass

    elif point_type == 0b10000011:
        pass

    elif point_type == 0b01000011:
        pass

    elif point_type == 0b00100011:
        pass

    elif point_type == 0b00010011:
        pass

    elif point_type == 0b00001011:
        pass

    elif point_type == 0b00000111:
        pass

    elif point_type == 0b11110000:
        pass

    elif point_type == 0b11101000:
        pass

    elif point_type == 0b11011000:
        pass

    elif point_type == 0b10111000:
        pass

    elif point_type == 0b01111000:
        pass

    elif point_type == 0b11100100:
        pass

    elif point_type == 0b11010100:
        pass

    elif point_type == 0b10110100:
        pass

    elif point_type == 0b01110100:
        pass

    elif point_type == 0b11001100:
        pass

    elif point_type == 0b10101100:
        pass

    elif point_type == 0b01101100:
        pass

    elif point_type == 0b10011100:
        pass

    elif point_type == 0b01011100:
        pass

    elif point_type == 0b00111100:
        pass

    elif point_type == 0b11100010:
        pass

    elif point_type == 0b11010010:
        pass

    elif point_type == 0b10110010:
        pass

    elif point_type == 0b01110010:
        pass

    elif point_type == 0b11001010:
        pass

    elif point_type == 0b10101010:
        pass

    elif point_type == 0b01101010:
        pass

    elif point_type == 0b10011010:
        pass

    elif point_type == 0b01011010:
        pass

    elif point_type == 0b00111010:
        pass

    elif point_type == 0b11000110:
        pass

    elif point_type == 0b10100110:
        pass

    elif point_type == 0b01100110:
        pass

    elif point_type == 0b10010110:
        pass

    elif point_type == 0b01010110:
        pass

    elif point_type == 0b00110110:
        pass

    elif point_type == 0b10001110:
        pass

    elif point_type == 0b01001110:
        pass

    elif point_type == 0b00101110:
        pass

    elif point_type == 0b00011110:
        pass

    elif point_type == 0b11100001:
        pass

    elif point_type == 0b11010001:
        pass

    elif point_type == 0b10110001:
        pass

    elif point_type == 0b01110001:
        pass

    elif point_type == 0b11001001:
        pass

    elif point_type == 0b10101001:
        pass

    elif point_type == 0b01101001:
        pass

    elif point_type == 0b10011001:
        pass

    elif point_type == 0b01011001:
        pass

    elif point_type == 0b00111001:
        pass

    elif point_type == 0b11000101:
        pass

    elif point_type == 0b10100101:
        pass

    elif point_type == 0b01100101:
        pass

    elif point_type == 0b10010101:
        pass

    elif point_type == 0b01010101:
        pass

    elif point_type == 0b00110101:
        pass

    elif point_type == 0b10001101:
        pass

    elif point_type == 0b01001101:
        pass

    elif point_type == 0b00101101:
        pass

    elif point_type == 0b00011101:
        pass

    elif point_type == 0b11000011:
        pass

    elif point_type == 0b10100011:
        pass

    elif point_type == 0b01100011:
        pass

    elif point_type == 0b10010011:
        pass

    elif point_type == 0b01010011:
        pass

    elif point_type == 0b00110011:
        pass

    elif point_type == 0b10001011:
        pass

    elif point_type == 0b01001011:
        pass

    elif point_type == 0b00101011:
        pass

    elif point_type == 0b00011011:
        pass

    elif point_type == 0b10000111:
        pass

    elif point_type == 0b01000111:
        pass

    elif point_type == 0b00100111:
        pass

    elif point_type == 0b00010111:
        pass

    elif point_type == 0b00001111:
        pass

    elif point_type == 0b11111000:
        pass

    elif point_type == 0b11110100:
        pass

    elif point_type == 0b11101100:
        pass

    elif point_type == 0b11011100:
        pass

    elif point_type == 0b10111100:
        pass

    elif point_type == 0b01111100:
        pass

    elif point_type == 0b11110010:
        pass

    elif point_type == 0b11101010:
        pass

    elif point_type == 0b11011010:
        pass

    elif point_type == 0b10111010:
        pass

    elif point_type == 0b01111010:
        pass

    elif point_type == 0b11100110:
        pass

    elif point_type == 0b11010110:
        pass

    elif point_type == 0b10110110:
        pass

    elif point_type == 0b01110110:
        pass

    elif point_type == 0b11001110:
        pass

    elif point_type == 0b10101110:
        pass

    elif point_type == 0b01101110:
        pass

    elif point_type == 0b10011110:
        pass

    elif point_type == 0b01011110:
        pass

    elif point_type == 0b00111110:
        pass

    elif point_type == 0b11110001:
        pass

    elif point_type == 0b11101001:
        pass

    elif point_type == 0b11011001:
        pass

    elif point_type == 0b10111001:
        pass

    elif point_type == 0b01111001:
        pass

    elif point_type == 0b11100101:
        pass

    elif point_type == 0b11010101:
        pass

    elif point_type == 0b10110101:
        pass

    elif point_type == 0b01110101:
        pass

    elif point_type == 0b11001101:
        pass

    elif point_type == 0b10101101:
        pass

    elif point_type == 0b01101101:
        pass

    elif point_type == 0b10011101:
        pass

    elif point_type == 0b01011101:
        pass

    elif point_type == 0b00111101:
        pass

    elif point_type == 0b11100011:
        pass

    elif point_type == 0b11010011:
        pass

    elif point_type == 0b10110011:
        pass

    elif point_type == 0b01110011:
        pass

    elif point_type == 0b11001011:
        pass

    elif point_type == 0b10101011:
        pass

    elif point_type == 0b01101011:
        pass

    elif point_type == 0b10011011:
        pass

    elif point_type == 0b01011011:
        pass

    elif point_type == 0b00111011:
        pass

    elif point_type == 0b11000111:
        pass

    elif point_type == 0b10100111:
        pass

    elif point_type == 0b01100111:
        pass

    elif point_type == 0b10010111:
        pass

    elif point_type == 0b01010111:
        pass

    elif point_type == 0b00110111:
        pass

    elif point_type == 0b10001111:
        pass

    elif point_type == 0b01001111:
        pass

    elif point_type == 0b00101111:
        pass

    elif point_type == 0b00011111:
        pass

    elif point_type == 0b11111100:
        pass

    elif point_type == 0b11111010:
        pass

    elif point_type == 0b11110110:
        pass

    elif point_type == 0b11101110:
        pass

    elif point_type == 0b11011110:
        pass

    elif point_type == 0b10111110:
        pass

    elif point_type == 0b01111110:
        pass

    elif point_type == 0b11111001:
        pass

    elif point_type == 0b11110101:
        pass

    elif point_type == 0b11101101:
        pass

    elif point_type == 0b11011101:
        pass

    elif point_type == 0b10111101:
        pass

    elif point_type == 0b01111101:
        pass

    elif point_type == 0b11110011:
        pass

    elif point_type == 0b11101011:
        pass

    elif point_type == 0b11011011:
        pass

    elif point_type == 0b10111011:
        pass

    elif point_type == 0b01111011:
        pass

    elif point_type == 0b11100111:
        pass

    elif point_type == 0b11010111:
        pass

    elif point_type == 0b10110111:
        pass

    elif point_type == 0b01110111:
        pass

    elif point_type == 0b11001111:
        pass

    elif point_type == 0b10101111:
        pass

    elif point_type == 0b01101111:
        pass

    elif point_type == 0b10011111:
        pass

    elif point_type == 0b01011111:
        pass

    elif point_type == 0b00111111:
        pass

    elif point_type == 0b11111110:
        pass

    elif point_type == 0b11111101:
        pass

    elif point_type == 0b11111011:
        pass

    elif point_type == 0b11110111:
        pass

    elif point_type == 0b11101111:
        pass

    elif point_type == 0b11011111:
        pass

    elif point_type == 0b10111111:
        pass

    elif point_type == 0b01111111:
        pass

    elif point_type == 0b11111111:
        pass

    else:
        return []


def to_faces(p, point_type):
    if point_type == 0:
        # 0 0 0 0 0 0 0 0 ~ 0
        #
        #   6     7
        # 4     5
        #   2     3
        # 0     1
        #
        #                   .  .  .
        #                   .  .  .
        #                   .  .  .
        #          .  .  .
        #          .  .  .
        #          .  .  .
        # .  .  .
        # .  .  .
        # .  .  .
        #
        return []

    elif point_type == 0b10000000:
        # 1 0 0 0 0 0 0 0 ~ 128
        #
        #   6     7
        # 4     5
        #   2     3
        # o     1
        #
        #                   .  .  .
        #                   .  .  .
        #                   .  .  .
        #          .  .  .
        #          .  .  .
        #          1  .  .
        # .  .  .
        # 2  .  .
        # .  0  .
        #

        return [
            4, p[0], p[1], p[2], p[0]
        ]

    elif point_type == 0b01000000:
        # 0 1 0 0 0 0 0 0
        #
        #   6     7
        # 4     5
        #   2     3
        # 0     o
        #
        #                   .  .  .
        #                   .  .  .
        #                   .  .  .
        #          .  .  .
        #          .  .  .
        #          .  .  1
        # .  .  .
        # .  .  2
        # .  0  .
        #

        return [
            4, p[0], p[1], p[2], p[0]
        ]

    elif point_type == 0b00100000:
        # 0 0 1 0 0 0 0 0
        #
        #   6     7
        # 4     5
        #   o     3
        # 0     1
        #
        #                   .  .  .
        #                   2  .  .
        #                   .  1  .
        #          .  .  .
        #          .  .  .
        #          0  .  .
        # .  .  .
        # .  .  .
        # .  .  .
        #

        return [
            4, p[0], p[1], p[2], p[0]
        ]

    elif point_type == 0b00010000:
        # 0 0 0 1 0 0 0 0
        #
        #   6     7
        # 4     5
        #   2     o
        # 0     1
        #
        #                   .  .  .
        #                   .  .  2
        #                   .  1  .
        #          .  .  .
        #          .  .  .
        #          .  .  0
        # .  .  .
        # .  .  .
        # .  .  .
        #

        return [
            4, p[0], p[1], p[2], p[0]
        ]

    elif point_type == 0b00001000:
        # 0 0 0 0 1 0 0 0
        #
        #   6     7
        # o     5
        #   2     3
        # 0     1
        #
        #                   .  .  .
        #                   .  .  .
        #                   .  .  .
        #          2  .  .
        #          .  .  .
        #          .  .  .
        # .  1  .
        # 0  .  .
        # .  .  .
        #

        return [
            4, p[0], p[1], p[2], p[0]
        ]

    elif point_type == 0b00000100:
        # 0 0 0 0 0 1 0 0
        #
        #   6     7
        # 4     o
        #   2     3
        # 0     1
        #
        #                   .  .  .
        #                   .  .  .
        #                   .  .  .
        #          .  .  2
        #          .  .  .
        #          .  .  .
        # .  1  .
        # .  .  0
        # .  .  .
        #

        return [
            4, p[0], p[1], p[2], p[0]
        ]

    elif point_type == 0b00000010:
        # 0 0 0 0 0 0 1 0
        #
        #   o     7
        # 4     5
        #   2     3
        # 0     1
        #
        #                   .  2  .
        #                   0  .  .
        #                   .  .  .
        #          1  .  .
        #          .  .  .
        #          .  .  .
        # .  .  .
        # .  .  .
        # .  .  .
        #

        return [
            4, p[0], p[1], p[2], p[0]
        ]

    elif point_type == 0b00000001:
        # 0 0 0 0 0 0 0 1
        #
        #   6     o
        # 4     5
        #   2     3
        # 0     1
        #
        #                   .  2  .
        #                   .  .  .
        #                   .  .  .
        #          .  .  1
        #          .  .  0
        #          .  .  .
        # .  .  .
        # .  .  .
        # .  .  .
        #

        return [
            4, p[0], p[1], p[2], p[0]
        ]

    elif point_type == 0b11000000:
        # 1 1 0 0 0 0 0 0
        #
        #   6     7
        # 4     5
        #   2     3
        # o     o
        #
        #                   .  .  .
        #                   .  .  .
        #                   .  .  .
        #          .  .  .
        #          .  .  .
        #          0  .  1
        # .  .  .
        # 2  .  3
        # .  .  .
        #
        return [
            4, p[0], p[1], p[2], p[0],
            4, p[1], p[2], p[3], p[1]
        ]

    elif point_type == 0b10100000:
        # 1 0 1 0 0 0 0 0
        #
        #   6     7
        # 4     5
        #   o     3
        # o     1
        #
        #                   .  .  .
        #                   3  .  .
        #                   .  1  .
        #          .  .  .
        #          .  .  .
        #          .  .  .
        # .  .  .
        # 2  .  .
        # .  0  .
        #
        return [
            4, p[0], p[1], p[2], p[0],
            4, p[1], p[2], p[3], p[1]
        ]

    elif point_type == 0b01100000:
        # 0 1 1 0 0 0 0 0
        #
        #   6     7
        # 4     5
        #   o     3
        # 0     o
        #
        #                   .  .  .
        #                   5  .  .
        #                   .  3  .
        #          .  .  .
        #          .  .  .
        #          1  .  2
        # .  .  .
        # .  .  4
        # .  0  .
        #
        return [
            4, p[0], p[2], p[4], p[0],
            4, p[1], p[3], p[5], p[1],
        ]

    elif point_type == 0b10010000:
        # 1 0 0 1 0 0 0 0
        #
        #   6     7
        # 4     5
        #   2     o
        # o     1
        #
        #                   .  .  .
        #                   .  .  5
        #                   .  3  .
        #          .  .  .
        #          .  .  .
        #          1  .  2
        # .  .  .
        # 4  .  .
        # .  0  .
        #

        return [
            4, p[0], p[1], p[4], p[0],
            4, p[2], p[3], p[5], p[2],
        ]

    elif point_type == 0b01010000:
        # 0 1 0 1 0 0 0 0
        #
        #   6     7
        # 4     5
        #   2     o
        # 0     o
        #
        #                   .  .  .
        #                   .  .  3
        #                   .  1  .
        #          .  .  .
        #          .  .  .
        #          .  .  .
        # .  .  .
        # .  .  2
        # .  0  .
        #
        #
        return [
            4, p[0], p[1], p[2], p[0],
            4, p[1], p[2], p[3], p[1],
        ]

    elif point_type == 0b00110000:
        # 0 0 1 1 0 0 0 0
        #
        #   6     7
        # 4     5
        #   o     o
        # 0     1
        #
        #                   .  .  .
        #                   2  .  3
        #                   .  .  .
        #          .  .  .
        #          .  .  .
        #          0  .  1
        # .  .  .
        # .  .  .
        # .  .  .
        #
        #
        return [
            4, p[0], p[1], p[2], p[0],
            4, p[1], p[2], p[3], p[1],
        ]

    elif point_type == 0b10001000:
        # 1 0 0 0 1 0 0 0
        #
        #   6     7
        # o     5
        #   2     3
        # o     1
        #
        #                   .  .  .
        #                   .  .  .
        #                   .  .  .
        #          3  .  .
        #          .  .  .
        #          1  .  .
        # .  2  .
        # .  .  .
        # .  0  .
        #
        return [
            4, p[0], p[1], p[2], p[0],
            4, p[1], p[2], p[3], p[1],
        ]

    elif point_type == 0b01001000:
        # 0 1 0 0 1 0 0 0
        #
        #   6     7
        # o     5
        #   2     3
        # 0     o
        #
        #                   .  .  .
        #                   .  .  .
        #                   .  .  .
        #          5  .  .
        #          .  .  .
        #          .  .  1
        # .  4  .
        # 2  .  3
        # .  0  .
        #
        return [
            4, p[0], p[1], p[3], p[0],
            4, p[2], p[4], p[5], p[2],
        ]

    elif point_type == 0b00101000:
        # 0 0 1 0 1 0 0 0
        #
        #   6     7
        # o     5
        #   o     3
        # 0     1
        #
        #                   .  .  .
        #                   3  .  .
        #                   .  1  .
        #          5  .  .
        #          .  .  .
        #          0  .  .
        # .  4  .
        # 2  .  .
        # .  .  .
        #
        return [
            4, p[0], p[1], p[3], p[0],
            4, p[2], p[4], p[5], p[2],
        ]

    elif point_type == 0b00011000:
        # 0 0 0 1 1 0 0 0
        #
        #   6     7
        # o     5
        #   2     o
        # 0     1
        #
        #                   .  .  .
        #                   .  .  3
        #                   .  1  .
        #          5  .  .
        #          .  .  .
        #          .  .  0
        # .  4  .
        # 2  .  .
        # .  .  .
        #
        return [
            4, p[0], p[1], p[3], p[0],
            4, p[2], p[4], p[5], p[2],
        ]

    elif point_type == 0b10000100:
        # 1 0 0 0 0 1 0 0
        #
        #   6     7
        # 4     o
        #   2     3
        # o     1
        #
        #                   .  .  .
        #                   .  .  .
        #                   .  .  .
        #          .  .  5
        #          .  .  .
        #          1  .  .
        # .  4  .
        # 2  .  3
        # .  0  .
        #
        return [
            4, p[0], p[1], p[2], p[0],
            4, p[3], p[4], p[5], p[3],
        ]

    elif point_type == 0b01000100:
        # 0 1 0 0 0 1 0 0
        #
        #   6     7
        # 4     o
        #   2     3
        # 0     o
        #
        #                   .  .  .
        #                   .  .  .
        #                   .  .  .
        #          .  .  3
        #          .  .  .
        #          .  .  1
        # .  2  .
        # .  .  .
        # .  0  .
        #
        return [
            4, p[0], p[1], p[2], p[0],
            4, p[1], p[2], p[3], p[1],
        ]

    elif point_type == 0b00100100:
        # 0 0 1 0 0 1 0 0
        #
        #   6     7
        # 4     o
        #   o     3
        # 0     1
        #
        #                   .  .  .
        #                   3  .  .
        #                   .  1  .
        #          .  .  5
        #          .  .  2
        #          0  .  .
        # .  4  .
        # .  .  .
        # .  .  .
        #
        return [
            4, p[0], p[1], p[3], p[0],
            4, p[2], p[4], p[5], p[2],
        ]

    elif point_type == 0b00010100:
        # 0 0 0 1 0 1 0 0
        #
        #   6     7
        # 4     o
        #   2     o
        # 0     1
        #
        #                   .  .  .
        #                   .  .  3
        #                   .  1  .
        #          .  .  5
        #          .  .  .
        #          .  .  0
        # .  4  .
        # .  .  2
        # .  .  .
        #
        return [
            4, p[0], p[1], p[3], p[0],
            4, p[2], p[4], p[5], p[2],
        ]

    elif point_type == 0b00001100:
        # 0 0 0 0 1 1 0 0
        #
        #   6     7
        # o     o
        #   2     3
        # 0     1
        #
        #                   .  .  .
        #                   .  .  .
        #                   .  .  .
        #          2  .  3
        #          .  .  .
        #          .  .  .
        # .  .  .
        # 0  .  1
        # .  .  .
        #
        return [
            4, p[0], p[1], p[2], p[0],
            4, p[1], p[2], p[3], p[1],
        ]

    elif point_type == 0b10000010:
        # 1 0 0 0 0 0 1 0
        #
        #   o     7
        # 4     5
        #   2     3
        # o     1
        #
        #                   .  5  .
        #                   3  .  .
        #                   .  .  .
        #          4  .  .
        #          1  .  .
        #          .  .  .
        # .  .  .
        # 2  .  .
        # .  0  .
        #
        return [
            4, p[0], p[1], p[2], p[0],
            4, p[3], p[4], p[5], p[3],
        ]

    elif point_type == 0b01000010:
        # 0 1 0 0 0 0 1 0
        #
        #   o     7
        # 4     5
        #   2     3
        # 0     o
        #
        #                   .  5  .
        #                   3  .  .
        #                   .  .  .
        #          4  .  .
        #          .  .  .
        #          .  .  1
        # .  .  .
        # .  .  2
        # .  0  .
        #
        return [
            4, p[0], p[1], p[2], p[0],
            4, p[3], p[4], p[5], p[3],
        ]

    elif point_type == 0b00100010:
        # 0 0 1 0 0 0 1 0
        #
        #   o     7
        # 4     5
        #   o      3
        # 0     1
        #
        #                   .  3  .
        #                   .  .  .
        #                   .  1  .
        #          2  .  .
        #          .  .  .
        #          0  .  .
        # .  .  .
        # .  .  .
        # .  .  .
        #
        return [
            4, p[0], p[1], p[2], p[0],
            4, p[1], p[2], p[3], p[1],
        ]

    elif point_type == 0b00010010:
        # 0 0 0 1 0 0 1 0
        #
        #   o     7
        # 4     5
        #   2     o
        # 0     1
        #
        #                   .  5  .
        #                   2  .  3
        #                   .  1  .
        #          4  .  .
        #          .  .  .
        #          .  .  0
        # .  .  .
        # .  .  .
        # .  .  .
        #
        return [
            4, p[0], p[1], p[3], p[0],
            4, p[2], p[4], p[5], p[2],
        ]

    elif point_type == 0b00001010:
        # 0 0 0 0 1 0 1 0
        #
        #   o     7
        # o     5
        #   2     3
        # 0     1
        #
        #                   .  3  .
        #                   1  .  .
        #                   .  .  .
        #          .  2  .
        #          0  .  .
        #          .  .  .
        # .  .  .
        # .  .  .
        # .  .  .
        #
        return [
            4, p[0], p[1], p[2], p[0],
            4, p[1], p[2], p[3], p[1],
        ]

    elif point_type == 0b00000110:
        # 0 0 0 0 0 1 1 0
        #
        #   o     7
        # 4     o
        #   2     3
        # 0     1
        #
        #                   .  5  .
        #                   1  .  .
        #                   .  .  .
        #          3  .  4
        #          .  .  .
        #          .  .  .
        # .  2  .
        # .  .  0
        # .  .  .
        #
        return [
            4, p[0], p[2], p[4], p[0],
            4, p[1], p[3], p[5], p[1],
        ]

    elif point_type == 0b10000001:
        # 1 0 0 0 0 0 0 1
        #
        #   6     o
        # 4     5
        #   2     3
        # o     1
        #
        #                   .  5  .
        #                   .  .  3
        #                   .  .  .
        #          .  .  4
        #          .  .  .
        #          1  .  .
        # .  .  .
        # 2  .  .
        # .  0  .
        #
        return [
            4, p[0], p[1], p[2], p[0],
            4, p[3], p[4], p[5], p[3],
        ]

    elif point_type == 0b01000001:
        # 0 1 0 0 0 0 0 1
        #
        #   6     o
        # 4     5
        #   2     3
        # 0     o
        #
        #                   .  5  .
        #                   .  .  3
        #                   .  .  .
        #          .  .  4
        #          .  .  .
        #          .  .  1
        # .  .  .
        # .  .  2
        # .  0  .
        #
        return [
            4, p[0], p[1], p[2], p[0],
            4, p[3], p[4], p[5], p[3],
        ]

    elif point_type == 0b00100001:
        # 0 0 1 0 0 0 0 1
        #
        #   6     o
        # 4     5
        #   o     3
        # 0     1
        #
        #                   .  5  .
        #                   2  .  3
        #                   .  1  .
        #          .  .  4
        #          .  .  .
        #          0  .  .
        # .  .  .
        # .  .  .
        # .  .  .
        #
        return [
            4, p[0], p[1], p[2], p[0],
            4, p[3], p[4], p[5], p[3],
        ]

    elif point_type == 0b00010001:
        # 0 0 0 0 0 0 0 1
        #
        #   6     o
        # 4     5
        #   2     o
        # 0     1
        #
        #                   .  3  .
        #                   .  .  .
        #                   .  1  .
        #          .  .  2
        #          .  .  .
        #          .  .  0
        # .  .  .
        # .  .  .
        # .  .  .
        #
        return [
            4, p[0], p[1], p[2], p[0],
            4, p[1], p[2], p[3], p[1],
        ]

    elif point_type == 0b00001001:
        # 0 0 0 0 1 0 0 1
        #
        #   6     o
        # o     5
        #   2     3
        # 0     1
        #
        #                   .  5  .
        #                   .  .  1
        #                   .  .  .
        #          3  .  4
        #          .  .  .
        #          .  .  .
        # .  2  .
        # 0  .  .
        # .  .  .
        #
        return [
            4, p[0], p[2], p[3], p[0],
            4, p[1], p[4], p[5], p[1],
        ]

    elif point_type == 0b00000101:
        # 0 0 0 0 0 1 0 1
        #
        #   6     o
        # 4     o
        #   2     3
        # 0     1
        #
        #                   .  3  .
        #                   .  .  1
        #                   .  .  .
        #          .  .  .
        #          .  .  .
        #          .  .  .
        # .  2  .
        # .  .  0
        # .  .  .
        #
        return [
            4, p[0], p[1], p[2], p[0],
            4, p[1], p[2], p[3], p[1],
        ]

    elif point_type == 0b00000011:
        # 0 0 0 0 0 0 1 1
        #
        #   o     o
        # 4     5
        #   2     3
        # 0     1
        #
        #                   .  .  .
        #                   0  .  1
        #                   .  .  .
        #          2  .  3
        #          .  .  .
        #          .  .  .
        # .  .  .
        # .  .  .
        # .  .  .
        #
        return [
            4, p[0], p[1], p[2], p[0],
            4, p[1], p[2], p[3], p[1],
        ]

    elif point_type == 0b11100000:
        # 1 1 1 0 0 0 0 0
        #
        #   6     7
        # 4      5
        #   o     3
        # o     o
        #
        #                   .  .  .
        #                   4  .  .
        #                   .  1  .
        #          .  .  .
        #          .  .  .
        #          .  .  0
        # .  .  .
        # 2  .  3
        # .  .  .
        #
        return [
            4, p[0], p[1], p[4], p[0],
            4, p[0], p[4], p[3], p[0],
            4, p[2], p[3], p[4], p[2],
        ]

    elif point_type == 0b11010000:
        # 1 1 0 1 0 0 0 0
        #
        #   6     7
        # 4     5
        #   2     o
        # o     o
        #
        #                   .  .  .
        #                   .  .  4
        #                   .  1  .
        #          .  .  .
        #          .  .  .
        #          0  .  .
        # .  .  .
        # 2  .  3
        # .  .  .
        #
        return [
            4, p[0], p[1], p[4], p[0],
            4, p[0], p[4], p[2], p[0],
            4, p[2], p[3], p[4], p[2],
        ]

    elif point_type == 0b10110000:
        # 1 0 1 1 0 0 0 0
        #
        #   6     7
        # 4     5
        #   o     o
        # o     1
        #
        #                   .  .  .
        #                   3  .  4
        #                   .  .  .
        #          .  .  .
        #          .  .  .
        #          .  .  1
        # .  .  .
        # 2  .  .
        # .  0  .
        #
        return [
            4, p[0], p[1], p[4], p[0],
            4, p[0], p[4], p[2], p[0],
            4, p[2], p[3], p[4], p[2],
        ]

    elif point_type == 0b01110000:
        # 0 1 1 1 0 0 0 0
        #
        #   6     7
        # 4     5
        #   o     o
        # 0     o
        #
        #                   .  .  .
        #                   3  .  4
        #                   .  .  .
        #          .  .  .
        #          .  .  .
        #          1  .  .
        # .  .  .
        # .  .  2
        # .  0  .
        #
        return [
            4, p[0], p[1], p[3], p[0],
            4, p[0], p[3], p[2], p[0],
            4, p[2], p[3], p[4], p[2],
        ]

    elif point_type == 0b11001000:
        # 1 1 0 0 1 0 0 0
        #
        #   6     7
        # o     5
        #   2     3
        # o     o
        #
        #                   .  .  .
        #                   .  .  .
        #                   .  .  .
        #          4  .  .
        #          .  .  .
        #          0  .  1
        # .  3  .
        # .  .  2
        # .  .  .
        #
        return [
            4, p[0], p[1], p[4], p[0],
            4, p[1], p[2], p[3], p[1],
            4, p[1], p[3], p[4], p[1],
        ]

    elif point_type == 0b10101000:
        # 1 0 1 0 1 0 0 0
        #
        #   6     7
        # o     5
        #   o     3
        # o     1
        #
        #                   .  .  .
        #                   .  .  .
        #                   .  .  .
        #          .  .  .
        #          .  .  .
        #          .  .  .
        # .  .  .
        # .  .  .
        # .  .  .
        #
        return [
            4, p[0], p[1], p[3], p[0],
            4, p[2], p[3], p[1], p[2],
            4, p[2], p[3], p[4], p[2],
        ]

    elif point_type == 0b01101000:
        # 0 1 1 0 1 0 0 0
        #
        #   6     7
        # o     5
        #   o     3
        # 0     o
        #
        #                   .  .  .
        #                   6  .  .
        #                   .  3  .
        #          8  .  .
        #          .  .  .
        #          1  .  2
        # .  7  .
        # 4  .  5
        # .  0  .
        return [
            4, p[0], p[2], p[5], p[0],
            4, p[1], p[3], p[6], p[1],
            4, p[4], p[7], p[8], p[4],
        ]

    elif point_type == 0b10011000:
        # 1 0 0 1 1 0 0 0
        #
        #   6     7
        # o     5
        #   2     o
        # o     1
        #
        #                   .  .  .
        #                   .  .  4
        #                   .  3  .
        #          .  .  .
        #          6  .  .
        #          1  .  2
        # .  5  .
        # .  .  .
        # .  0  .
        #
        return [
            4, p[0], p[1], p[5], p[0],
            4, p[1], p[5], p[6], p[1],
            4, p[2], p[3], p[4], p[2],
        ]

    elif point_type == 0b01011000:
        # 0 1 0 1 1 0 0 0
        #
        #   6     7
        # o     5
        #   2     o
        # 0     o
        #
        #                   .  .  .
        #                   .  .  5
        #                   .  1  .
        #          6  .  .
        #          .  .  .
        #          .  .  .
        # .  4  .
        # 2  .  3
        # .  0  .
        #
        return [
            4, p[0], p[1], p[3], p[0],
            4, p[1], p[3], p[5], p[1],
            4, p[2], p[4], p[6], p[2],
        ]

    elif point_type == 0b00111000:
        # 0 0 1 1 1 0 0 0
        #
        #   6     7
        # o     5
        #   o     o
        # 0     1
        #
        #                   .  .  .
        #                   3  .  4
        #                   .  .  .
        #          6  .  .
        #          .  .  .
        #          0  .  1
        # .  5  .
        # 2  .  .
        # .  .  .
        #
        return [
            4, p[0], p[1], p[3], p[0],
            4, p[1], p[3], p[4], p[1],
            4, p[2], p[5], p[6], p[2],
        ]

    elif point_type == 0b11000100:
        # 1 1 0 0 0 1 0 0
        #
        #   6     7
        # 4     o
        #   2     3
        # o     o
        #
        #                   .  .  .
        #                   .  .  .
        #                   .  .  .
        #          .  .  4
        #          .  .  .
        #          0  .  1
        # .  3  .
        # 2  .  .
        # .  .  .
        #
        return [
            4, p[0], p[1], p[4], p[0],
            4, p[0], p[2], p[3], p[0],
            4, p[0], p[3], p[4], p[0],
        ]

    elif point_type == 0b10100100:
        # 1 0 1 0 0 1 0 0
        #
        #   6     7
        # 4     o
        #   o     3
        # o     1
        #
        #                   .  .  .
        #                   4  .  .
        #                   .  1  .
        #          .  .  6
        #          .  .  3
        #          .  .  .
        # .  5  .
        # 2  .  .
        # .  0  .
        #
        return [
            4, p[0], p[1], p[2], p[0],
            4, p[1], p[2], p[4], p[1],
            4, p[3], p[5], p[6], p[3],
        ]

    elif point_type == 0b01100100:
        # 0 1 1 0 0 1 0 0
        #
        #   6     7
        # 4     o
        #   o     3
        # 0     o
        #
        #                   .  6  .
        #                   2  .  .
        #                   .  .  .
        #          4  .  5
        #          .  .  .
        #          .  .  1
        # .  3  .
        # .  .  .
        # .  0  .
        #
        return [
            4, p[0], p[1], p[3], p[0],
            4, p[1], p[3], p[5], p[1],
            4, p[2], p[4], p[6], p[2],
        ]

    elif point_type == 0b10010100:
        pass

    elif point_type == 0b01010100:
        pass

    elif point_type == 0b00110100:
        pass

    elif point_type == 0b10001100:
        pass

    elif point_type == 0b01001100:
        pass

    elif point_type == 0b00101100:
        pass

    elif point_type == 0b00011100:
        pass

    elif point_type == 0b11000010:
        pass

    elif point_type == 0b10100010:
        pass

    elif point_type == 0b01100010:
        pass

    elif point_type == 0b10010010:
        pass

    elif point_type == 0b01010010:
        pass

    elif point_type == 0b00110010:
        pass

    elif point_type == 0b10001010:
        pass

    elif point_type == 0b01001010:
        pass

    elif point_type == 0b00101010:
        pass

    elif point_type == 0b00011010:
        pass

    elif point_type == 0b10000110:
        pass

    elif point_type == 0b01000110:
        pass

    elif point_type == 0b00100110:
        pass

    elif point_type == 0b00010110:
        pass

    elif point_type == 0b00001110:
        pass

    elif point_type == 0b11000001:
        pass

    elif point_type == 0b10100001:
        pass

    elif point_type == 0b01100001:
        pass

    elif point_type == 0b10010001:
        pass

    elif point_type == 0b01010001:
        pass

    elif point_type == 0b00110001:
        pass

    elif point_type == 0b10001001:
        pass

    elif point_type == 0b01001001:
        pass

    elif point_type == 0b00101001:
        pass

    elif point_type == 0b00011001:
        pass

    elif point_type == 0b10000101:
        pass

    elif point_type == 0b01000101:
        pass

    elif point_type == 0b00100101:
        pass

    elif point_type == 0b00010101:
        pass

    elif point_type == 0b00001101:
        pass

    elif point_type == 0b10000011:
        pass

    elif point_type == 0b01000011:
        pass

    elif point_type == 0b00100011:
        pass

    elif point_type == 0b00010011:
        pass

    elif point_type == 0b00001011:
        pass

    elif point_type == 0b00000111:
        pass

    elif point_type == 0b11110000:
        pass

    elif point_type == 0b11101000:
        pass

    elif point_type == 0b11011000:
        pass

    elif point_type == 0b10111000:
        pass

    elif point_type == 0b01111000:
        pass

    elif point_type == 0b11100100:
        pass

    elif point_type == 0b11010100:
        pass

    elif point_type == 0b10110100:
        pass

    elif point_type == 0b01110100:
        pass

    elif point_type == 0b11001100:
        pass

    elif point_type == 0b10101100:
        pass

    elif point_type == 0b01101100:
        pass

    elif point_type == 0b10011100:
        pass

    elif point_type == 0b01011100:
        pass

    elif point_type == 0b00111100:
        pass

    elif point_type == 0b11100010:
        pass

    elif point_type == 0b11010010:
        pass

    elif point_type == 0b10110010:
        pass

    elif point_type == 0b01110010:
        pass

    elif point_type == 0b11001010:
        pass

    elif point_type == 0b10101010:
        pass

    elif point_type == 0b01101010:
        pass

    elif point_type == 0b10011010:
        pass

    elif point_type == 0b01011010:
        pass

    elif point_type == 0b00111010:
        pass

    elif point_type == 0b11000110:
        pass

    elif point_type == 0b10100110:
        pass

    elif point_type == 0b01100110:
        pass

    elif point_type == 0b10010110:
        pass

    elif point_type == 0b01010110:
        pass

    elif point_type == 0b00110110:
        pass

    elif point_type == 0b10001110:
        pass

    elif point_type == 0b01001110:
        pass

    elif point_type == 0b00101110:
        pass

    elif point_type == 0b00011110:
        pass

    elif point_type == 0b11100001:
        pass

    elif point_type == 0b11010001:
        pass

    elif point_type == 0b10110001:
        pass

    elif point_type == 0b01110001:
        pass

    elif point_type == 0b11001001:
        pass

    elif point_type == 0b10101001:
        pass

    elif point_type == 0b01101001:
        pass

    elif point_type == 0b10011001:
        pass

    elif point_type == 0b01011001:
        pass

    elif point_type == 0b00111001:
        pass

    elif point_type == 0b11000101:
        pass

    elif point_type == 0b10100101:
        pass

    elif point_type == 0b01100101:
        pass

    elif point_type == 0b10010101:
        pass

    elif point_type == 0b01010101:
        pass

    elif point_type == 0b00110101:
        pass

    elif point_type == 0b10001101:
        pass

    elif point_type == 0b01001101:
        pass

    elif point_type == 0b00101101:
        pass

    elif point_type == 0b00011101:
        pass

    elif point_type == 0b11000011:
        pass

    elif point_type == 0b10100011:
        pass

    elif point_type == 0b01100011:
        pass

    elif point_type == 0b10010011:
        pass

    elif point_type == 0b01010011:
        pass

    elif point_type == 0b00110011:
        pass

    elif point_type == 0b10001011:
        pass

    elif point_type == 0b01001011:
        pass

    elif point_type == 0b00101011:
        pass

    elif point_type == 0b00011011:
        pass

    elif point_type == 0b10000111:
        pass

    elif point_type == 0b01000111:
        pass

    elif point_type == 0b00100111:
        pass

    elif point_type == 0b00010111:
        pass

    elif point_type == 0b00001111:
        pass

    elif point_type == 0b11111000:
        pass

    elif point_type == 0b11110100:
        pass

    elif point_type == 0b11101100:
        pass

    elif point_type == 0b11011100:
        pass

    elif point_type == 0b10111100:
        pass

    elif point_type == 0b01111100:
        pass

    elif point_type == 0b11110010:
        pass

    elif point_type == 0b11101010:
        pass

    elif point_type == 0b11011010:
        pass

    elif point_type == 0b10111010:
        pass

    elif point_type == 0b01111010:
        pass

    elif point_type == 0b11100110:
        pass

    elif point_type == 0b11010110:
        pass

    elif point_type == 0b10110110:
        pass

    elif point_type == 0b01110110:
        pass

    elif point_type == 0b11001110:
        pass

    elif point_type == 0b10101110:
        pass

    elif point_type == 0b01101110:
        pass

    elif point_type == 0b10011110:
        pass

    elif point_type == 0b01011110:
        pass

    elif point_type == 0b00111110:
        pass

    elif point_type == 0b11110001:
        pass

    elif point_type == 0b11101001:
        pass

    elif point_type == 0b11011001:
        pass

    elif point_type == 0b10111001:
        pass

    elif point_type == 0b01111001:
        pass

    elif point_type == 0b11100101:
        pass

    elif point_type == 0b11010101:
        pass

    elif point_type == 0b10110101:
        pass

    elif point_type == 0b01110101:
        pass

    elif point_type == 0b11001101:
        pass

    elif point_type == 0b10101101:
        pass

    elif point_type == 0b01101101:
        pass

    elif point_type == 0b10011101:
        pass

    elif point_type == 0b01011101:
        pass

    elif point_type == 0b00111101:
        pass

    elif point_type == 0b11100011:
        pass

    elif point_type == 0b11010011:
        pass

    elif point_type == 0b10110011:
        pass

    elif point_type == 0b01110011:
        pass

    elif point_type == 0b11001011:
        pass

    elif point_type == 0b10101011:
        pass

    elif point_type == 0b01101011:
        pass

    elif point_type == 0b10011011:
        pass

    elif point_type == 0b01011011:
        pass

    elif point_type == 0b00111011:
        pass

    elif point_type == 0b11000111:
        pass

    elif point_type == 0b10100111:
        pass

    elif point_type == 0b01100111:
        pass

    elif point_type == 0b10010111:
        pass

    elif point_type == 0b01010111:
        pass

    elif point_type == 0b00110111:
        pass

    elif point_type == 0b10001111:
        pass

    elif point_type == 0b01001111:
        pass

    elif point_type == 0b00101111:
        pass

    elif point_type == 0b00011111:
        pass

    elif point_type == 0b11111100:
        pass

    elif point_type == 0b11111010:
        pass

    elif point_type == 0b11110110:
        pass

    elif point_type == 0b11101110:
        pass

    elif point_type == 0b11011110:
        pass

    elif point_type == 0b10111110:
        pass

    elif point_type == 0b01111110:
        pass

    elif point_type == 0b11111001:
        pass

    elif point_type == 0b11110101:
        pass

    elif point_type == 0b11101101:
        pass

    elif point_type == 0b11011101:
        pass

    elif point_type == 0b10111101:
        pass

    elif point_type == 0b01111101:
        pass

    elif point_type == 0b11110011:
        pass

    elif point_type == 0b11101011:
        pass

    elif point_type == 0b11011011:
        pass

    elif point_type == 0b10111011:
        pass

    elif point_type == 0b01111011:
        pass

    elif point_type == 0b11100111:
        pass

    elif point_type == 0b11010111:
        pass

    elif point_type == 0b10110111:
        pass

    elif point_type == 0b01110111:
        pass

    elif point_type == 0b11001111:
        pass

    elif point_type == 0b10101111:
        pass

    elif point_type == 0b01101111:
        pass

    elif point_type == 0b10011111:
        pass

    elif point_type == 0b01011111:
        pass

    elif point_type == 0b00111111:
        pass

    elif point_type == 0b11111110:
        pass

    elif point_type == 0b11111101:
        pass

    elif point_type == 0b11111011:
        pass

    elif point_type == 0b11110111:
        pass

    elif point_type == 0b11101111:
        pass

    elif point_type == 0b11011111:
        pass

    elif point_type == 0b10111111:
        pass

    elif point_type == 0b01111111:
        pass

    elif point_type == 0b11111111:
        pass

    else:
        return []