from turtle import *
import math

# Name your Turtle.
tiffany = Turtle()

# Set Up your screen and starting position.
setup(500,300)
x_pos = 0
y_pos = 0
tiffany.setposition(x_pos, y_pos)

### Write your code below:

#This allows for the user to choose the color
color_choice = ["red","orange","yellow","green","blue","purple"]
color = input('Enter a color:')
tiffany.pencolor(color)

#This allows for the user to choose the number of sides of the shape
#This does not yet work
shape_sides = ["3","4","5","6"]
sides = input('Enter a number of sides:')
int ???

for shape in range(sides):
    tiffany.forward(100)
    tiffany.right(360/sides)

#This draws a square
for square in range(4):
    tiffany.pendown()
    tiffany.forward(100)
    tiffany.right(90)

for move in range(1):
    tiffany.penup()
    tiffany.forward(100)

#This draws a triangle
for triangle in range(3):
    tiffany.pendown()
    tiffany.forward(100)
    tiffany.left(120)





# Close window on click.
exitonclick()
