import turtle
from turtle import Turtle
from square import Square
from walk import Walk
from Spirograph import Spirograph


# square_draw = Square(Turtle())
# square_draw.draw(10)
# square_draw.draw_multiple(10, [1,3,4,5,6,7,8,9,10])

walk_draw = Walk(Turtle())
walk_draw.walk(10, 20)

turtle.colormode(255)
spirograph_draw = Spirograph(Turtle())
spirograph_draw.draw(5)


turtle.Screen().exitonclick()


