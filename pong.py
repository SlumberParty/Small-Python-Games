import turtle

win = turtle.Screen()
win.title("Pooong by Claire")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("hotpink")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B


# Ball


# main game loop
while True:
    win.update()
