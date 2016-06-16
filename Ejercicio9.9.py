import turtle
t = turtle.Pen()

nLado = int(input('Ingrese el numero de lados (rango: 3 a 20): '))
tLado = int(input('Ingrese el tamaño de los lados (rango: 10 a 500): '))

def mipoligono(num, tam):
	for x in range(1, num+1):
		t.forward(tam)
		t.left(360/num)

mipoligono(nLado, tLado)
turtle.getscreen()._root.mainloop()