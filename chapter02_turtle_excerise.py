import turtle

turtle.speed(3)

#defining draw big star function
def drawbigstar(length):
    turtle.begin_fill()
    for side in range(5):
        turtle.forward(length)
        turtle.left(72)
        turtle.forward(length)
        turtle.right(144)
    turtle.end_fill()
    turtle.up()

#to move the pen aside
turtle.down()
turtle.penup()
turtle.left(90)
turtle.forward(300)
turtle.left(90)
turtle.forward(300)

#to set the color of flag
turtle.color("red", "red")
turtle.begin_fill()

#start drawing the flag
turtle.down()
for side in range(2):
    turtle.left(90)
    turtle.forward(200)

    turtle.left(90)
    turtle.forward(300)

turtle.end_fill()

#now the stars
turtle.penup()
turtle.left(90)
turtle.forward(40)
turtle.left(90)
turtle.forward(20)

#to set the color of the stars
turtle.color("yellow", "yellow")

#start drawing the stars
turtle.down()
drawbigstar(20)

#moving the pen to start drawing small stars
turtle.forward(70)
turtle.left(90)
turtle.forward(15)
turtle.setheading(32)

#draw small star
turtle.down()
drawbigstar(9)

#2nd small star 
turtle.setheading(270)
turtle.forward(42)
turtle.left(90)

turtle.down()
drawbigstar(9)

turtle.done()
