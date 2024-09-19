class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def falls_in_rectangle(self, lowleft, upright):
        if lowleft[0] < self.x < upright[0] \
            and lowleft[1] < self.y < upright[1]:
            return True
        else:
            return False

point1 = Point(5, 6)
point2 = Point(7, 9)
point3 = Point(3, 4)

print(point3.falls_in_rectangle((5,6), (7,9)))
# TypeError: 'Point' object is not subscriptable
# print(point3.falls_in_rectangle(point1, point2))

print(point3.falls_in_rectangle((1,1), (6,6)))
