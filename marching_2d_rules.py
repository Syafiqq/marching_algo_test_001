import numpy as np
import pyvista as pv


def __mid_point(p1, p2):
    pt = abs(p1 - p2) / 2
    return p1 + pt


def to_poly(points, point_type):
    if point_type == 0:
        # 0 0 0 0 ~ 0
        #
        # . . .
        # . . .
        # . . .
        return None

    elif point_type == 8:
        # 1 0 0 0 ~ 8
        #
        # . . .
        # . . .
        # 1 . .
        p0 = points[0]
        p1 = __mid_point(points[0], points[1])
        p2 = __mid_point(points[0], points[2])

        points = [p0, p1, p2]
        faces = [4, 0, 1, 2, 0]
        return pv.PolyData(points, faces=faces)

    elif point_type == 4:
        # 0 1 0 0 ~ 4
        #
        # . . .
        # . . .
        # . . 1
        p0 = __mid_point(points[0], points[1])
        p1 = points[1]
        p2 = __mid_point(points[1], points[3])

        points = [p0, p1, p2]
        faces = [4, 0, 1, 2, 0]
        return pv.PolyData(points, faces=faces)

    elif point_type == 2:
        # 0 0 1 0 ~ 2
        #
        # 1 . .
        # . . .
        # . . .
        p0 = __mid_point(points[0], points[2])
        p1 = points[2]
        p2 = __mid_point(points[2], points[3])

        points = [p0, p1, p2]
        faces = [4, 0, 1, 2, 0]
        return pv.PolyData(points, faces=faces)

    elif point_type == 1:
        # 0 0 0 1 ~ 1
        #
        # . . 1
        # . . .
        # . . .
        p0 = __mid_point(points[1], points[3])
        p1 = __mid_point(points[2], points[3])
        p2 = points[3]

        points = [p0, p1, p2]
        faces = [4, 0, 1, 2, 0]
        return pv.PolyData(points, faces=faces)

    elif point_type == 12:
        # 1 1 0 0 ~ 12
        #
        # . . .
        # . . .
        # 1 . 1
        p0 = points[0]
        p2 = points[1]
        p1 = __mid_point(points[0], points[1])
        p3 = __mid_point(points[0], points[2])
        p5 = __mid_point(points[1], points[3])
        p4 = __mid_point(p3, p5)

        points = [p0, p1, p2, p3, p4, p5]
        faces = np.array([
            # . . .
            # 3 . .
            # 0 1 .
            [4, 0, 1, 3, 0],
            # . . .
            # 3 4 .
            # . 1 .
            [4, 1, 3, 4, 1],
            # . . .
            # . 4 5
            # . 1 .
            [4, 1, 4, 5, 1],
            # . . .
            # . . 5
            # . 1 2
            [4, 1, 2, 5, 1]
        ]).flatten()
        return pv.PolyData(points, faces=faces)

    elif point_type == 10:
        # 1 0 1 0 ~ 10
        #
        # 1 . .
        # . . .
        # 1 . .
        p0 = points[0]
        p1 = __mid_point(points[0], points[1])
        p2 = __mid_point(points[0], points[2])
        p3 = __mid_point(p2, __mid_point(points[1], points[3]))
        p4 = points[2]
        p5 = __mid_point(points[2], points[3])

        points = [p0, p1, p2, p3, p4, p5]
        faces = np.array([
            # . . .
            # 2 . .
            # 0 1 .
            [4, 2, 0, 1, 2],
            # . . .
            # 2 3 .
            # . 1 .
            [4, 1, 2, 3, 1],
            # 4 5 .
            # 2 . .
            # . . .
            [4, 2, 4, 5, 2],
            # . 5 .
            # 2 3 .
            # . . .
            [4, 2, 3, 5, 2]
        ]).flatten()
        return pv.PolyData(points, faces=faces)

    elif point_type == 3:
        # 0 0 1 1 ~ 3
        #
        # 1 . 1
        # . . .
        # . . .
        p0 = __mid_point(points[0], points[2])
        p2 = __mid_point(points[1], points[3])
        p1 = __mid_point(p0, p2)
        p3 = points[2]
        p4 = __mid_point(points[2], points[3])
        p5 = points[3]

        points = [p0, p1, p2, p3, p4, p5]
        faces = np.array([
            # . 4 .
            # 0 1 .
            # . . .
            [4, 0, 1, 4, 0],
            # 3 4 .
            # 0 . .
            # . . .
            [4, 0, 3, 4, 0],
            # . 4 .
            # . 1 2
            # . . .
            [4, 1, 2, 4, 1],
            # . 4 5
            # . . 2
            # . . .
            [4, 2, 4, 5, 2]
        ]).flatten()
        return pv.PolyData(points, faces=faces)

    elif point_type == 5:
        # 0 1 0 1 ~ 5
        #
        # . . 1
        # . . .
        # . . 1
        p0 = __mid_point(points[0], points[1])
        p1 = points[1]
        p3 = __mid_point(points[1], points[3])
        p2 = __mid_point(__mid_point(points[0], points[2]), p3)
        p4 = __mid_point(points[2], points[3])
        p5 = points[3]

        points = [p0, p1, p2, p3, p4, p5]
        faces = np.array([
            # . . .
            # . . 3
            # . 0 1
            [4, 0, 1, 3, 0],
            # . . .
            # . 2 3
            # . 0 .
            [4, 0, 2, 3, 0],
            # . 4 .
            # . 2 3
            # . . .
            [4, 2, 3, 4, 2],
            # . 4 5
            # . . 3
            # . , .
            [4, 3, 4, 5, 3]
        ]).flatten()
        return pv.PolyData(points, faces=faces)

    elif point_type == 9:
        # 1 0 0 1 ~ 9
        #
        # . . 1
        # . . .
        # 1 . .
        p0 = points[0]
        p1 = __mid_point(points[0], points[1])
        p2 = __mid_point(points[0], points[2])
        p3 = __mid_point(points[1], points[3])
        p4 = __mid_point(points[2], points[3])
        p5 = points[3]

        points = [p0, p1, p2, p3, p4, p5]
        faces = np.array([
            # . . .
            # 2 . .
            # 0 1 .
            [4, 0, 1, 2, 0],
            # . 4 5
            # . . 3
            # . . .
            [4, 3, 4, 5, 3],
        ]).flatten()
        return pv.PolyData(points, faces=faces)

    elif point_type == 6:
        # 0 1 1 0 ~ 6
        #
        # 1 . .
        # . . .
        # . . 1
        p0 = __mid_point(points[0], points[1])
        p1 = points[1]
        p2 = __mid_point(points[1], points[3])
        p3 = __mid_point(points[0], points[2])
        p4 = points[2]
        p5 = __mid_point(points[2], points[3])

        points = [p0, p1, p2, p3, p4, p5]
        faces = np.array([
            # . . .
            # . . 2
            # . 0 1
            [4, 0, 1, 2, 0],
            # 4 5 .
            # 3 . .
            # . . .
            [4, 3, 4, 5, 3],
        ]).flatten()
        return pv.PolyData(points, faces=faces)

    elif point_type == 14:
        # 1 1 1 0 ~ 14
        #
        # 1 . .
        # . . .
        # 1 . 1
        p0 = points[0]
        p1 = __mid_point(points[0], points[1])
        p2 = points[1]
        p3 = __mid_point(points[0], points[2])
        p5 = __mid_point(points[1], points[3])
        p4 = __mid_point(p3, p5)
        p6 = points[2]
        p7 = __mid_point(points[2], points[3])

        points = [p0, p1, p2, p3, p4, p5, p6, p7]
        faces = np.array([
            # . . .
            # 3 . .
            # 0 1 .
            [4, 0, 1, 3, 0],
            # . . .
            # 3 4 .
            # . 1 .
            [4, 1, 3, 4, 1],
            # . . .
            # . 4 5
            # . 1 .
            [4, 1, 4, 5, 1],
            # . . .
            # . . 5
            # . 1 2
            [4, 1, 2, 5, 1],
            # 6 7 .
            # 3 . .
            # . . .
            [4, 3, 6, 7, 3],
            # . 7 .
            # 3 4 .
            # . . .
            [4, 3, 4, 7, 3],
            # . 7 .
            # . 4 5
            # . . .
            [4, 4, 5, 7, 4]

        ]).flatten()
        return pv.PolyData(points, faces=faces)

    elif point_type == 13:
        # 1 1 0 1 ~ 13
        #
        # . . 1
        # . . .
        # 1 . 1
        p0 = points[0]
        p1 = __mid_point(points[0], points[1])
        p2 = points[1]
        p3 = __mid_point(points[0], points[2])
        p5 = __mid_point(points[1], points[3])
        p4 = __mid_point(p3, p5)
        p6 = __mid_point(points[2], points[3])
        p7 = points[3]

        points = [p0, p1, p2, p3, p4, p5, p6, p7]
        faces = np.array([
            # . . .
            # 3 . .
            # 0 1 .
            [4, 0, 1, 3, 0],
            # . . .
            # 3 4 .
            # . 1 .
            [4, 1, 3, 4, 1],
            # . . .
            # . 4 5
            # . 1 .
            [4, 1, 4, 5, 1],
            # . . .
            # . . 5
            # . 1 2
            [4, 1, 2, 5, 1],
            # . 6 .
            # 3 4 .
            # . . .
            [4, 3, 4, 6, 3],
            # . 6 .
            # . 4 5
            # . . .
            [4, 4, 5, 6, 4],
            # . 6 7
            # . . 5
            # . . .
            [4, 5, 6, 7, 5]

        ]).flatten()
        return pv.PolyData(points, faces=faces)

    elif point_type == 7:
        # 0 1 1 1 ~ 7
        #
        # 1 . 1
        # . . .
        # . . 1
        p0 = __mid_point(points[0], points[1])
        p1 = points[1]
        p2 = __mid_point(points[0], points[2])
        p4 = __mid_point(points[1], points[3])
        p3 = __mid_point(p2, p4)
        p5 = points[2]
        p6 = __mid_point(points[2], points[3])
        p7 = points[3]

        points = [p0, p1, p2, p3, p4, p5, p6, p7]
        faces = np.array([
            # . . .
            # 2 3 .
            # . 0 .
            [4, 0, 2, 3, 0],
            # . . .
            # . . 4
            # . 0 1
            [4, 0, 1, 4, 0],
            # . . .
            # . 3 4
            # . 0 .
            [4, 0, 3, 4, 0],
            # 5 6 .
            # 2 . .
            # . . .
            [4, 2, 5, 6, 2],
            # . 6 .
            # 2 3 .
            # . . .
            [4, 2, 3, 6, 2],
            # . 6 .
            # . 3 4
            # . . .
            [4, 3, 4, 6, 3],
            # . 6 7
            # . . 4
            # . . .
            [4, 4, 6, 7, 6]
        ]).flatten()
        return pv.PolyData(points, faces=faces)

    elif point_type == 11:
        # 1 0 1 1 ~ 1
        #
        # 1 . 1
        # . . .
        # 1 . .
        p0 = points[0]
        p1 = __mid_point(points[0], points[1])
        p2 = __mid_point(points[0], points[2])
        p4 = __mid_point(points[1], points[3])
        p3 = __mid_point(p2, p4)
        p5 = points[2]
        p6 = __mid_point(points[2], points[3])
        p7 = points[3]

        points = [p0, p1, p2, p3, p4, p5, p6, p7]
        faces = np.array([
            # . . .
            # 2 . .
            # 0 1 .
            [4, 0, 1, 2, 0],
            # . . .
            # 2 3 .
            # . 1 .
            [4, 1, 2, 3, 1],
            # . . .
            # . 3 4
            # . 1 .
            [4, 1, 3, 4, 1],
            # . 6 .
            # 2 3 .
            # . . .
            [4, 2, 3, 6, 2],
            # 5 6 .
            # 2 . .
            # . . .
            [4, 2, 5, 6, 2],
            # . 6 .
            # . 3 4
            # . . .
            [4, 3, 4, 6, 3],
            # . 6 7
            # . . 4
            # . . .
            [4, 4, 6, 7, 6]

        ]).flatten()
        return pv.PolyData(points, faces=faces)

    elif point_type == 15:
        # 1 1 1 1 ~ 15
        #
        # 1 . 1
        # . . .
        # 1 . 1
        p0 = points[0]
        p1 = __mid_point(points[0], points[1])
        p2 = points[1]
        p3 = __mid_point(points[0], points[2])
        p5 = __mid_point(points[1], points[3])
        p4 = __mid_point(p3, p5)
        p6 = points[2]
        p7 = __mid_point(points[2], points[3])
        p8 = points[3]

        points = [p0, p1, p2, p3, p4, p5, p6, p7, p8]
        faces = np.array([
            # . . .
            # 3 . .
            # 0 1 .
            [4, 0, 1, 3, 0],
            # . . .
            # 3 4 .
            # . 1 .
            [4, 1, 3, 4, 1],
            # . . .
            # . 4 5
            # . 1 .
            [4, 1, 4, 5, 1],
            # . . .
            # . . 5
            # . 1 2
            [4, 1, 2, 5, 1],
            # . 7 .
            # 3 4 .
            # . . .
            [4, 3, 4, 7, 3],
            # 6 7 .
            # 3 . .
            # . . .
            [4, 3, 6, 7, 3],
            # . 7 .
            # . 4 5
            # . . .
            [4, 4, 5, 7, 4],
            # . 7 8
            # . . 5
            # . . .
            [4, 5, 7, 8, 5]

        ]).flatten()
        return pv.PolyData(points, faces=faces)


def to_points(points, point_type):
    if point_type == 0:
        # 0 0 0 0 ~ 0
        #
        # . . .
        # . . .
        # . . .
        points = []
        return points

    elif point_type == 8:
        # 1 0 0 0 ~ 8
        #
        # . . .
        # . . .
        # 1 . .
        p0 = points[0]
        p1 = __mid_point(points[0], points[1])
        p2 = __mid_point(points[0], points[2])

        points = [p0, p1, p2]
        return points

    elif point_type == 4:
        # 0 1 0 0 ~ 4
        #
        # . . .
        # . . .
        # . . 1
        p0 = __mid_point(points[0], points[1])
        p1 = points[1]
        p2 = __mid_point(points[1], points[3])

        points = [p0, p1, p2]
        return points

    elif point_type == 2:
        # 0 0 1 0 ~ 2
        #
        # 1 . .
        # . . .
        # . . .
        p0 = __mid_point(points[0], points[2])
        p1 = points[2]
        p2 = __mid_point(points[2], points[3])

        points = [p0, p1, p2]
        return points

    elif point_type == 1:
        # 0 0 0 1 ~ 1
        #
        # . . 1
        # . . .
        # . . .
        p0 = __mid_point(points[1], points[3])
        p1 = __mid_point(points[2], points[3])
        p2 = points[3]

        points = [p0, p1, p2]
        return points

    elif point_type == 12:
        # 1 1 0 0 ~ 12
        #
        # . . .
        # . . .
        # 1 . 1
        p0 = points[0]
        p2 = points[1]
        p1 = __mid_point(points[0], points[1])
        p3 = __mid_point(points[0], points[2])
        p5 = __mid_point(points[1], points[3])
        p4 = __mid_point(p3, p5)

        points = [p0, p1, p2, p3, p4, p5]
        return points

    elif point_type == 10:
        # 1 0 1 0 ~ 10
        #
        # 1 . .
        # . . .
        # 1 . .
        p0 = points[0]
        p1 = __mid_point(points[0], points[1])
        p2 = __mid_point(points[0], points[2])
        p3 = __mid_point(p2, __mid_point(points[1], points[3]))
        p4 = points[2]
        p5 = __mid_point(points[2], points[3])

        points = [p0, p1, p2, p3, p4, p5]
        return points

    elif point_type == 3:
        # 0 0 1 1 ~ 3
        #
        # 1 . 1
        # . . .
        # . . .
        p0 = __mid_point(points[0], points[2])
        p2 = __mid_point(points[1], points[3])
        p1 = __mid_point(p0, p2)
        p3 = points[2]
        p4 = __mid_point(points[2], points[3])
        p5 = points[3]

        points = [p0, p1, p2, p3, p4, p5]
        return points

    elif point_type == 5:
        # 0 1 0 1 ~ 5
        #
        # . . 1
        # . . .
        # . . 1
        p0 = __mid_point(points[0], points[1])
        p1 = points[1]
        p3 = __mid_point(points[1], points[3])
        p2 = __mid_point(__mid_point(points[0], points[2]), p3)
        p4 = __mid_point(points[2], points[3])
        p5 = points[3]

        points = [p0, p1, p2, p3, p4, p5]
        return points

    elif point_type == 9:
        # 1 0 0 1 ~ 9
        #
        # . . 1
        # . . .
        # 1 . .
        p0 = points[0]
        p1 = __mid_point(points[0], points[1])
        p2 = __mid_point(points[0], points[2])
        p3 = __mid_point(points[1], points[3])
        p4 = __mid_point(points[2], points[3])
        p5 = points[3]

        points = [p0, p1, p2, p3, p4, p5]
        return points

    elif point_type == 6:
        # 0 1 1 0 ~ 6
        #
        # 1 . .
        # . . .
        # . . 1
        p0 = __mid_point(points[0], points[1])
        p1 = points[1]
        p2 = __mid_point(points[1], points[3])
        p3 = __mid_point(points[0], points[2])
        p4 = points[2]
        p5 = __mid_point(points[2], points[3])

        points = [p0, p1, p2, p3, p4, p5]
        return points

    elif point_type == 14:
        # 1 1 1 0 ~ 14
        #
        # 1 . .
        # . . .
        # 1 . 1
        p0 = points[0]
        p1 = __mid_point(points[0], points[1])
        p2 = points[1]
        p3 = __mid_point(points[0], points[2])
        p5 = __mid_point(points[1], points[3])
        p4 = __mid_point(p3, p5)
        p6 = points[2]
        p7 = __mid_point(points[2], points[3])

        points = [p0, p1, p2, p3, p4, p5, p6, p7]
        return points

    elif point_type == 13:
        # 1 1 0 1 ~ 13
        #
        # . . 1
        # . . .
        # 1 . 1
        p0 = points[0]
        p1 = __mid_point(points[0], points[1])
        p2 = points[1]
        p3 = __mid_point(points[0], points[2])
        p5 = __mid_point(points[1], points[3])
        p4 = __mid_point(p3, p5)
        p6 = __mid_point(points[2], points[3])
        p7 = points[3]

        points = [p0, p1, p2, p3, p4, p5, p6, p7]
        return points

    elif point_type == 7:
        # 0 1 1 1 ~ 7
        #
        # 1 . 1
        # . . .
        # . . 1
        p0 = __mid_point(points[0], points[1])
        p1 = points[1]
        p2 = __mid_point(points[0], points[2])
        p4 = __mid_point(points[1], points[3])
        p3 = __mid_point(p2, p4)
        p5 = points[2]
        p6 = __mid_point(points[2], points[3])
        p7 = points[3]

        points = [p0, p1, p2, p3, p4, p5, p6, p7]
        return points

    elif point_type == 11:
        # 1 0 1 1 ~ 1
        #
        # 1 . 1
        # . . .
        # 1 . .
        p0 = points[0]
        p1 = __mid_point(points[0], points[1])
        p2 = __mid_point(points[0], points[2])
        p4 = __mid_point(points[1], points[3])
        p3 = __mid_point(p2, p4)
        p5 = points[2]
        p6 = __mid_point(points[2], points[3])
        p7 = points[3]

        points = [p0, p1, p2, p3, p4, p5, p6, p7]
        return points

    elif point_type == 15:
        # 1 1 1 1 ~ 15
        #
        # 1 . 1
        # . . .
        # 1 . 1
        p0 = points[0]
        p1 = __mid_point(points[0], points[1])
        p2 = points[1]
        p3 = __mid_point(points[0], points[2])
        p5 = __mid_point(points[1], points[3])
        p4 = __mid_point(p3, p5)
        p6 = points[2]
        p7 = __mid_point(points[2], points[3])
        p8 = points[3]

        points = [p0, p1, p2, p3, p4, p5, p6, p7, p8]
        return points
