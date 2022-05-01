import turtle

turtle.shape('turtle')

#Draw square counterclock-wise
def draw_left():
    turtle.left(90)
    turtle.forward(50)


def main():
    for i in range(4):
        draw_left()


"""
#Draw S use functions
def draw_left():
    turtle.left(90)
    turtle.forward(50)

def draw_right():
    turtle.right(90)
    turtle.forward(50)

def main():
    turtle.forward(50)
    draw_left()
    draw_left()

    draw_right()
    draw_right()

#Draw S use step by step commands
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
"""
main()
turtle.done()