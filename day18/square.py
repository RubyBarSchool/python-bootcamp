######## Challenge 1 - Draw a Square #########
import random
from color import turtle_color

class Square:
    def __init__(self,turtle):
        self.turtle = turtle
        self.turtle.speed("fastest")
        self.turtle.color("black")
        self.turtle.pensize(1)
        self.turtle.shape("turtle")

    def draw(self,length, corner=90):
        # self.resize_screen(length)
        for _ in range(int(360/corner)):
            for i in range(length):
                if i % 2 == 0:
                    self.turtle.color(random.choice(turtle_color))
                    self.turtle.pendown()
                    self.turtle.begin_fill()
                    self.turtle.circle(10)
                    self.turtle.end_fill()
                    self.turtle.penup()
                self.turtle.forward(20)
            self.turtle.left(corner)

    def draw_multiple(self,length,amount):
        for i in amount:
            self.draw(length, 360/i)

    # def resize_screen(self, length):
        # self.turtle.turtlesize(100, 100)
        # self.turtle.screen.setup(length + 50, length + 50)
        # self.turtle.screen.screensize(length, length)