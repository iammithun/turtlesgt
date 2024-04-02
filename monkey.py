# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 17:46:59 2024

@author: iamrs
"""

import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Monkey Drawing")
screen.setup(width=600, height=600)
screen.bgcolor("lightblue")

# Create a turtle
monkey = turtle.Turtle()
monkey.speed(0)  # Set the drawing speed to the fastest

# Draw the monkey's face
monkey.penup()
monkey.goto(0, -200)
monkey.pendown()
monkey.begin_fill()
monkey.circle(200)
monkey.end_fill()

# Draw the monkey's eyes
monkey.penup()
monkey.goto(-100, 50)
monkey.pendown()
monkey.begin_fill()
monkey.circle(40)
monkey.end_fill()

monkey.penup()
monkey.goto(100, 50)
monkey.pendown()
monkey.begin_fill()
monkey.circle(40)
monkey.end_fill()

# Draw the monkey's nose
monkey.penup()
monkey.goto(0, 50)
monkey.pendown()
monkey.begin_fill()
monkey.circle(25)
monkey.end_fill()

# Draw the monkey's mouth
monkey.penup()
monkey.goto(-100, -20)
monkey.pendown()
monkey.setheading(-60)
monkey.circle(70, 120)

# Hide the turtle
monkey.hideturtle()

# Keep the window open
screen.mainloop()
