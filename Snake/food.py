from turtle import Turtle
import random

coords = []
for i in range(-260, 280, 20):
    coords.append(i)

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.6, 0.6)
        self.color("red")
        self.setpos((random.choice(coords), random.choice(coords)))

    def refresh(self):
        self.setpos((random.choice(coords), random.choice(coords)))