from turtle import *  # Import the turtle tool

yellow_oct = Turtle()  # Assigning the 5th octagon turtle
yellow_oct.color("yellow")  # Assigning the color of the 5th octagon
yellow_oct.ht()  # Hiding the turtle
yellow_oct.pu()  # Putting the pen up
yellow_oct.setpos(0, -50)  # Setting the (x,y) position
yellow_oct.pd()  # Putting the pen down
for i in range(8):  # Starting drawing the 5th octagon
    yellow_oct.forward(50)  # Go forward 50 units
    yellow_oct.right(45)  # Go right angle 45

green_oct = Turtle()  # Assigning the 4th octagon turtle
green_oct.color("sea green")  # Assigning the color of the 4th octagon
green_oct.ht()  # Hiding the turtle
green_oct.pu()  # Putting the pen up
green_oct.setpos(0, 0)  # Setting the (x,y) position
green_oct.pd()  # Putting the pen down
for i in range(8):  # Starting drawing the 4th octagon
    green_oct.forward(50)  # Go forward 50 units
    green_oct.right(45)  # Go right angle 45

red_oct = Turtle()  # Assigning the 3rd octagon turtle
red_oct.color("red")  # Assigning the color of the 3rd octagon
red_oct.ht()  # Hiding the turtle
red_oct.pu()  # Putting the pen up
red_oct.setpos(0, 100)  # Setting the (x,y) position
red_oct.pd()  # Putting the pen down
for i in range(8):  # Starting drawing the 3rd octagon
    red_oct.forward(50)  # Go forward 50 units
    red_oct.right(45)  # Go right angle 45

blue_oct = Turtle()  # Assigning the 2nd octagon turtle
blue_oct.color("blue")  # Assigning the color of the 2nd octagon
blue_oct.ht()  # Hiding the turtle
blue_oct.pu()  # Putting the pen up
blue_oct.setpos(0, 125)  # Setting the (x,y) position
blue_oct.pd()  # Putting the pen down
for i in range(8):  # Starting drawing the 2nd octagon
    blue_oct.forward(50)  # Go forward 50 units
    blue_oct.right(45)  # Go right angle 45

darkRed_oct = Turtle()  # Assigning the 1st octagon turtle
darkRed_oct.color("dark red")  # Assigning the 1st octagon color
darkRed_oct.ht()  # Hiding the turtle
darkRed_oct.pu()  # Putting the pen up
darkRed_oct.setpos(0, 150)  # Setting the (x,y) position
darkRed_oct.pd()  # Putting the pen down
for i in range(8):  # Starting drawing the 1st octagon
    darkRed_oct.forward(50)  # Go forward 50 units
    darkRed_oct.right(45)  # Go right angle 45

dot1 = Turtle()  # Assigning the dot on the lift
dot1.color("yellow", "black")  # Assigning the color of the dot on the lift
dot1.begin_fill()  # Filling the dot
dot1.ht()  # Hiding the turtle
dot1.pu()  # Putting the pen up
dot1.setpos(4, 60)  # Setting the (x,y) position
dot1.pd()  # Putting the pen down
dot1.circle(5)  # The area of the circle
dot1.end_fill()  # Stop filling the dot

dot2 = Turtle()  # Assigning the dot on the right
dot2.color("yellow", "black")  # Assigning the color of the dot on the right
dot2.begin_fill()  # Filling the dot
dot2.ht()  # Hiding the turtle
dot2.pu()  # Putting up the pen
dot2.setpos(48, 60)  # Setting the (x,y) position
dot2.pd()  # Putting the pen down
dot2.circle(5)  # The area of the circle
dot2.end_fill()  # Stop filling the dot

done() # keep window open

