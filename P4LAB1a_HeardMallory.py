import turtle
t = turtle.Turtle()

for x in ['blue', 'red', 'blue', 'red']:
    t.color(x)
    t.forward(75)
    t.left(90)

for y in ['green', 'orange', 'brown']:
    t.color(y)
    t.forward(75)
    t.left(120)
turtle.done()

 