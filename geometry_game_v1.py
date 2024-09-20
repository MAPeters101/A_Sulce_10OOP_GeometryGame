from random import randint
import turtle

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.point1.x < self.x < rectangle.point2.x \
        and rectangle.point1.y < self.y < rectangle.point2.y:
            return True
        else:
            return False


class Rectangle:

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return (self.point2.x - self.point1.x) * (self.point2.y - self.point1.y)


class GUIRectangle(Rectangle):

    def draw(self, canvas):
        # Go to a certain coordinate
        canvas.penup()
        canvas.goto(self.point1.x, self.point1.y)

        # Draw a rectangle
        canvas.pendown()
        canvas.forward(100)
        canvas.left(90)
        canvas.forward(200)
        canvas.left(90)
        canvas.forward(100)
        canvas.left(90)
        canvas.forward(200)
        canvas.left(90)

        turtle.done()


gui_rectangle = GUIRectangle(Point(randint(0, 400), randint(0, 400)),
                Point(randint(10, 400), randint(10, 400)))

myTurtle = turtle.Turtle()

gui_rectangle.draw(canvas=myTurtle)
print(gui_rectangle.area())

# rectangle = Rectangle(
#     Point(randint(0, 400), randint(0, 400)),
#     Point(randint(10, 400), randint(10, 400))
# )
#
# print("Rectangle Coordinates: ",
#       rectangle.point1.x, ",",
#       rectangle.point1.y, "and",
#       rectangle.point2.x, ",",
#       rectangle.point2.y)
#
# user_point = Point(float(input("Guess X: ")),
#                    float(input("Guess Y: ")))
#
# print("Your point was inside rectangle: ",
#       user_point.falls_in_rectangle(rectangle))
#
# user_area = float(input("Guess rectangle area: "))
#
# print("Your area was off by: ", rectangle.area() - user_area)
# print("The actual area was: ", rectangle.area())