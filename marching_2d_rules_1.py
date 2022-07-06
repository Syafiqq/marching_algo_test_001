def __mid_point(p1, p2):
    pt = abs(p1 - p2) / 2
    return p1 + pt


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
        p1 = points[1]
        p2 = __mid_point(points[0], points[2])
        p3 = __mid_point(points[1], points[3])

        points = [p0, p1, p2, p3]
        return points

    elif point_type == 10:
        # 1 0 1 0 ~ 10
        #
        # 1 . .
        # . . .
        # 1 . .
        p0 = points[0]
        p1 = __mid_point(points[0], points[1])
        p2 = points[2]
        p3 = __mid_point(points[2], points[3])

        points = [p0, p1, p2, p3]
        return points

    elif point_type == 3:
        # 0 0 1 1 ~ 3
        #
        # 1 . 1
        # . . .
        # . . .
        p0 = __mid_point(points[0], points[2])
        p1 = __mid_point(points[1], points[3])
        p2 = points[2]
        p3 = points[3]

        points = [p0, p1, p2, p3]
        return points

    elif point_type == 5:
        # 0 1 0 1 ~ 5
        #
        # . . 1
        # . . .
        # . . 1
        p0 = __mid_point(points[0], points[1])
        p1 = points[1]
        p2 = __mid_point(points[2], points[3])
        p3 = points[3]

        points = [p0, p1, p2, p3]
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
        p1 = points[1]
        p2 = __mid_point(points[1], points[3])
        p3 = points[2]
        p4 = __mid_point(points[2], points[3])

        points = [p0, p1, p2, p3, p4]
        return points

    elif point_type == 13:
        # 1 1 0 1 ~ 13
        #
        # . . 1
        # . . .
        # 1 . 1
        p0 = points[0]
        p1 = points[1]
        p2 = __mid_point(points[0], points[2])
        p3 = __mid_point(points[2], points[3])
        p4 = points[3]

        points = [p0, p1, p2, p3, p4]
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
        p3 = points[2]
        p4 = points[3]

        points = [p0, p1, p2, p3, p4]
        return points

    elif point_type == 11:
        # 1 0 1 1 ~ 1
        #
        # 1 . 1
        # . . .
        # 1 . .
        p0 = points[0]
        p1 = __mid_point(points[0], points[1])
        p2 = __mid_point(points[1], points[3])
        p3 = points[2]
        p4 = points[3]

        points = [p0, p1, p2, p3, p4]
        return points

    elif point_type == 15:
        # 1 1 1 1 ~ 15
        #
        # 1 . 1
        # . . .
        # 1 . 1
        p0 = points[0]
        p1 = points[1]
        p2 = points[2]
        p3 = points[3]

        points = [p0, p1, p2, p3]
        return points


def to_faces(p, point_type):
    if point_type == 0:
        # 0 0 0 0 ~ 0
        #
        # . . .
        # . . .
        # . . .
        faces = []
        return faces

    elif point_type == 8:
        # 1 0 0 0 ~ 8
        #
        # . . .
        # . . .
        # 1 . .

        faces = [
            # . . .
            # 2 . .
            # 0 1 .
            [4, p[0], p[1], p[2], p[0]]
        ]
        return faces

    elif point_type == 4:
        # 0 1 0 0 ~ 4
        #
        # . . .
        # . . .
        # . . 1

        faces = [
            # . . .
            # . . 2
            # . 0 1
            [4, p[0], p[1], p[2], p[0]]
        ]
        return faces

    elif point_type == 2:
        # 0 0 1 0 ~ 2
        #
        # 1 . .
        # . . .
        # . . .

        faces = [
            # 1 2 .
            # 0 . .
            # . . .
            [4, p[0], p[1], p[2], p[0]]
        ]
        return faces

    elif point_type == 1:
        # 0 0 0 1 ~ 1
        #
        # . . 1
        # . . .
        # . . .

        faces = [
            # . 1 2
            # . . 0
            # . . .
            [4, p[0], p[1], p[2], p[0]]
        ]
        return faces

    elif point_type == 12:
        # 1 1 0 0 ~ 12
        #
        # . . .
        # . . .
        # 1 . 1

        faces = [
            # . . .
            # . . 3
            # 0 . 1
            [4, p[0], p[1], p[3], p[0]],
            # . . .
            # 2 . 3
            # 0 . .
            [4, p[0], p[2], p[3], p[0]],
        ]
        return faces

    elif point_type == 10:
        # 1 0 1 0 ~ 10
        #
        # 1 . .
        # . . .
        # 1 . .

        faces = [
            # . 3 .
            # . . .
            # 0 1 .
            [4, p[0], p[1], p[3], p[0]],
            # 2 3 .
            # . . .
            # 0 . .
            [4, p[0], p[2], p[3], p[0]],
        ]
        return faces

    elif point_type == 3:
        # 0 0 1 1 ~ 3
        #
        # 1 . 1
        # . . .
        # . . .

        faces = [
            # . . 3
            # 0 . 1
            # . . .
            [4, p[0], p[1], p[3], p[0]],
            # 2 . 3
            # 0 . .
            # . . .
            [4, p[0], p[2], p[3], p[0]],
        ]
        return faces

    elif point_type == 5:
        # 0 1 0 1 ~ 5
        #
        # . . 1
        # . . .
        # . . 1

        faces = [
            # . . 3
            # . . .
            # . 0 1
            [4, p[0], p[1], p[3], p[0]],
            # . 2 3
            # . . .
            # . 0 .
            [4, p[0], p[2], p[3], p[0]],
        ]
        return faces

    elif point_type == 9:
        # 1 0 0 1 ~ 9
        #
        # . . 1
        # . . .
        # 1 . .

        faces = [
            # . . .
            # 2 . .
            # 0 1 .
            [4, p[0], p[1], p[2], p[0]],
            # . 4 5
            # . . 3
            # . . .
            [4, p[3], p[4], p[5], p[3]],
        ]
        return faces

    elif point_type == 6:
        # 0 1 1 0 ~ 6
        #
        # 1 . .
        # . . .
        # . . 1

        faces = [
            # . . .
            # . . 2
            # . 0 1
            [4, p[0], p[1], p[2], p[0]],
            # 4 5 .
            # 3 . .
            # . . .
            [4, p[3], p[4], p[5], p[3]],
        ]
        return faces

    elif point_type == 14:
        # 1 1 1 0 ~ 14
        #
        # 1 . .
        # . . .
        # 1 . 1

        faces = [
            # . . .
            # . . 2
            # 0 . 1
            [4, p[0], p[1], p[2], p[0]],
            # . 4 .
            # . . 2
            # 0 . .
            [4, p[0], p[2], p[4], p[0]],
            # 3 4 .
            # . . .
            # 0 . .
            [4, p[0], p[3], p[4], p[0]],
        ]
        return faces

    elif point_type == 13:
        # 1 1 0 1 ~ 13
        #
        # . . 1
        # . . .
        # 1 . 1

        faces = [
            # . . .
            # 2 . .
            # 0 . 1
            [4, p[0], p[1], p[2], p[0]],
            # . 3 .
            # 2 . .
            # . . 1
            [4, p[1], p[2], p[3], p[1]],
            # . 3 4
            # . . .
            # . . 1
            [4, p[1], p[3], p[4], p[1]],
        ]
        return faces

    elif point_type == 7:
        # 0 1 1 1 ~ 7
        #
        # 1 . 1
        # . . .
        # . . 1

        faces = [
            # . . 4
            # . . .
            # . 0 1
            [4, p[0], p[1], p[4], p[0]],
            # . . 4
            # 2 . .
            # . 0 .
            [4, p[0], p[2], p[4], p[0]],
            # 3 . 4
            # 2 . .
            # . . .
            [4, p[2], p[3], p[4], p[2]],
        ]
        return faces

    elif point_type == 11:
        # 1 0 1 1 ~ 1
        #
        # 1 . 1
        # . . .
        # 1 . .

        faces = [
            # 3 . 4
            # . . 2
            # 0 1 .
            [4, p[0], p[1], p[3], p[0]],
            # 3 . 4
            # . . 2
            # 0 1 .
            [4, p[1], p[2], p[3], p[1]],
            # 3 . 4
            # . . 2
            # 0 1 .
            [4, p[2], p[3], p[4], p[2]],
        ]
        return faces

    elif point_type == 15:
        # 1 1 1 1 ~ 15
        #
        # 1 . 1
        # . . .
        # 1 . 1
        faces = [
            # . . 3
            # . . .
            # 0 . 1
            [4, p[0], p[1], p[3], p[0]],
            # 2 . 3
            # . . .
            # 0 . .
            [4, p[0], p[2], p[3], p[0]],
        ]
        return faces
