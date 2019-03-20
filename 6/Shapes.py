import turtle
pen=turtle.Turtle()
size=float(input("size?"))
sides=int(input("sides?"))
for i in range(sides):
    pen.forward(size)
    pen.left(360/sides)
    
pen.clear()
for i in range(5):
    pen.forward(100)
    pen.left(180-36)
pen.right(90-36/2)
pen.circle(52)
