import turtle
t = turtle.Turtle()
t.shape("turtle")

def square(length):
    t.down()
    for i in range(4):
        t.forward(length)
        t.left(90)
    t.up()

square(100)

turtle.done()

