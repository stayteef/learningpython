# this is to learn what 'loop' is. 

import turtle
turtle.down()
for side in range(4):
    turtle.forward(100)
    turtle.right(90)

#so in X in range (Y) is to tell the program how many times it has to run the thing. here it is 4 so it means 0 1 2 3, 4 times in total.

turtle.down()
for side in range(4):
    print(side)
    turtle.forward(100)
    turtle.right(90)
#in terminal it prints 0 1 2 3

for side in range(30):
    turtle.forward(100)
    turtle.right(30 + side)
#here the arrow turns a little more everytime it turns 

turtle.down()
for side in range(56,61):
    print(side)
    turtle.forward(100)
    turtle.right(144)
#i drew a star here! also i used 55-61, also is like 5 times. in print you can see it's actully 56 57 58 59 60.



