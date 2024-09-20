from turtle import Turtle

#Create a canvas instance
t = Turtle()

# Go to a certain coordinate
t.penup()
t.goto(50, 75)

# Draw a rectangle
t.pendown()
t.forward(100)
t.left(90)
t.forward(200)
t.left(90)
t.forward(100)
t.left(90)
t.forward(200)
t.left(90)


t.screen.mainloop()