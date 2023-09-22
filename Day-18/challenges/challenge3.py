# TODO: Draw random walk challenge

import  turtle as t

tim = t.Turtle()
t.colormode(255)

import  random
colors = ["dark turquoise", "cyan", "dark green", "lime green", "brown",
		"wheat", "indianred","skyblue", "indigo", "purple", "tomato"]

directions = [0,90,180,270]
tim.pensize(15)
tim.speed("fastest")


for _ in range(200):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(directions))