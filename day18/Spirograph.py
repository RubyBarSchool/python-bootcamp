######## Challenge 5 - Draw a Spirograph #########

import random

class Spirograph:
    def __init__(self,turtle):
        self.turtle = turtle
        self.turtle.speed("fastest")
        self.turtle.pensize(2)
        self.turtle.shape("turtle")

    def draw(self,angle):
        for _ in range(int(360/angle)):
            self.turtle.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
            self.turtle.circle(100)
            self.turtle.setheading(self.turtle.heading() + angle)