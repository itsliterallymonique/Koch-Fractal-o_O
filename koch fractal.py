import turtle

def koch_fract(turtle, divis, size):
    if divis == 0:
        turtle.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_fract(turtle, divis - 1, size / 3)
            turtle.left(angle)

divis = 10
size = 2000

wn = turtle.Screen()
wn.setup(width=1000, height=500)

turtle.penup()
turtle.goto(-500, 150)

turtle.speed(100)
            
turtle.pendown()

for i in range(0, 3):
    koch_fract(turtle, divis, size)
    turtle.left(-120)
