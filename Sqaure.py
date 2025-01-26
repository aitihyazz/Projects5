import turtle
turtle.Screen().bgcolor("blue")
turtle.Screen().setup(300,400)
square=turtle.Turtle()
sides= 4
side_lenght=100
angle =360 /sides
for i in range(sides):
    square.forward(side_lenght)
    square.right(angle)
turtle.done()