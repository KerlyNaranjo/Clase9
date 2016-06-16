from tkinter import *
tk = Tk()

canvas = Canvas(tk, widt = 400, height = 400)
canvas.pack()
canvas.create_polygon(10, 10, 10, 60, 50, 35)
#my_image = PhotoImage(file='ball.gif')
#canvas.my_image

def movetriangle(event):
	if event.keysym == 'Up':
		canvas.move(1, 0, -3)
	elif event.keysym == 'Down':
		canvas.move(1, 0, 3)
	elif event.keysym == 'Left':
		canvas.move(1, -3, 0)
	else:
		canvas.move(1, 3, 0)
		#(1, x, y)

canvas.bind_all('<KeyPress-Up>', movetriangle)
canvas.bind_all('<KeyPress-Down>', movetriangle)
canvas.bind_all('<KeyPress-Left>', movetriangle)
canvas.bind_all('<KeyPress-Right>', movetriangle)
tk.mainloop()