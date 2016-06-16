import turtle
t = turtle.Pen()

t.reset()

for x in range(1, 9):
	t.forward(100)
	t.left(225)

turtle.getscreen()._root.mainloop()