import turtle
t = turtle.Pen()

def micuadrado(size):
	for x in range(1, 12):
		t.forward(size)
		t.left(90)

#micuadrado(100)

t.forward(10)
t.left(90)
t.forward(50)
t.left(45+180)
t.forward(60)

t.left(45)
t.forward(10)
t.left(135)
t.forward(60)

t.left(270)
t.forward(60)

t.left(90)
t.forward(10)

t.left(90)
t.forward(60)

t.left(225)
t.forward(60)

t.left(90)
t.forward(10)

t.left(90)
t.forward(120)




turtle.getscreen()._root.mainloop()