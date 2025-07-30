from turtle import Turtle, Screen


STARTING = [(0,0), (-20,0), (-40,0)]
DISTANCE = 20

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for pos in STARTING:
            self.add_segment(pos)

    def add_segment(self, position):
        s = Turtle()
        s.color("white")
        s.shape("square")
        s.penup()
        s.setpos(position)
        self.segments.append(s)

    def reset(self):
        for seg in self.segments:
            seg.goto(500,500)
        self.segments.clear()
        self.create_snake()

    def extend(self):
        self.add_segment(self.segments[-1].pos())


    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            self.segments[seg].setpos(self.segments[seg - 1].pos())
        self.segments[0].forward(DISTANCE)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)