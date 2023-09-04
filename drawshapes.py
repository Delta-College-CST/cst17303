import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle object
pen = turtle.Turtle()

# Draw a square
pen.penup()
pen.goto(-200, 200)
pen.pendown()
pen.forward(100)
pen.right(90)
pen.forward(100)
pen.right(90)
pen.forward(100)
pen.right(90)
pen.forward(100)
pen.right(90)

# Draw an equilateral triangle
pen.penup()
pen.goto(0, 200)
pen.pendown()
pen.forward(100)
pen.left(120)
pen.forward(100)
pen.left(120)
pen.forward(100)
pen.left(120)

# Draw a rectangle
pen.penup()
pen.goto(200, 200)
pen.pendown()
pen.goto(250, 200)
pen.goto(250, 0)
pen.goto(200, 0)
pen.goto(200, 200)

# Park pen at origin (middle)
pen.penup()
pen.goto(0, 0)
