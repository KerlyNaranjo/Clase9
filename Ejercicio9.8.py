import turtle
t = turtle.Pen()

n = int(input('Ingrese el tamaño de lso lados: '))

def micuadrado(size):
	for x in range(1, 5):
		t.forward(size)
		t.left(90)

micuadrado(n)
turtle.getscreen()._root.mainloop()
