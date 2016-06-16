import turtle
t = turtle.Pen()

t.reset()
n = int(input('Ingrese el numero de lados: '))

for x in range(1, n+1):
	t.forward(100)
	t.left(360/n)

turtle.getscreen()._root.mainloop()