import turtle

turtle.speed(3)

#defining draw star function
def drawstar(length):
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
for _ in range(2):
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
drawstar(20)

#moving the pen to start drawing small stars
turtle.forward(70)
turtle.left(90)
turtle.forward(15)
turtle.setheading(32)

#draw small star
turtle.down()
drawstar(9)

#2nd small star 
turtle.setheading(270)
turtle.forward(16)
turtle.setheading(0)
turtle.forward(20)
turtle.setheading(10)

turtle.down()
drawstar(9)

#3nd small star 
turtle.setheading(270)
turtle.forward(30)
turtle.setheading(0)
turtle.setheading(10)
turtle.down()
drawstar(9)

#third star
turtle.setheading(270)
turtle.forward(15)
turtle.setheading(180)
turtle.forward(20)
turtle.setheading(320)
turtle.down()
drawstar(9)

turtle.up()
turtle.forward(400)
turtle.done()