######## Challenge 4 - Random walk #########
import random
from color import turtle_color

class Walk:
    def __init__(self,turtle):
        self.turtle = turtle
        self.turtle.color("black")
        self.turtle.pensize(5)
        self.turtle.shape("turtle")

    def walk(self, length, amount):
        for i in range(length):
            walk_type = random.choice(['forward', 'backward', 'left', 'right'])
            walk_move = random.choice(['forward', 'backward'])
            self.turtle.color(random.choice(turtle_color))
            match walk_type:
                case 'forward':
                    self.turtle.forward(amount)
                case 'backward':
                    self.turtle.backward(amount)
                case 'left':
                    self.turtle.left(90)
                    self.walk_multiple(amount, walk_move)
                case 'right':
                    self.turtle.right(90)
                    self.walk_multiple(amount, walk_move)

    def walk_multiple(self,length,type_move):
        match type_move:
            case "forward":
                self.turtle.forward(length)
            case "backward":
                self.turtle.backward(length)