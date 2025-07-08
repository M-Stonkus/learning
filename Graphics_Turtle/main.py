from turtle import Turtle, Screen
import random
import matplotlib.pyplot as plt

screen= Screen()
screen.colormode(255)

dot = Turtle()
dot.shape("arrow")
dot.pencolor("white")
dot.pensize(5)
#dot.sety(250)
dot.speed(15)

colors = ["blue", "red", "purple", "green", "orange", "black"]

#draws shapes
shape = False
if shape:
    for i in range(3,11):
        dot.pencolor((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
        for j in range(i):
            dot.forward(0.5)
            dot.right(360/i)



#random walk
x_dist = []
walk = False
if walk:
    for i in range(200):
        dot.pencolor((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
        dot.right(random.choice([0, 90, 180, 270]))
        dot.forward(5)
        x_dist.append(dot.xcor())

    #should be normal distribution??? I guess 10000 steps is not enough and takes too long with drawing
    plt.hist(x_dist, density=True, bins=20)
    plt.show()

#spirograph
spirograph = True
if spirograph:
    dot.pensize(2.5)
    for _ in range(500):
        dot.color((random.randint(180, 255), random.randint(0, 185), random.randint(0, 185)))
        dot.circle(200)
        dot.right(360/500*7)





screen.exitonclick()