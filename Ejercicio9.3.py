import turtle
t = turtle.Pen()

t.forward(50)
t.left(45)
t.forward(100)
t.left(90)
t.forward(50)
t.right(45)
t.forward(100)

turtle.getscreen()._root.mainloop()

t.reset()
for x in range(1, 9):
	t.forward(100)
	t.left(225)