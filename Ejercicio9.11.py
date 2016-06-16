from tkinter import *
tk = Tk()

canvas = Canvas(tk, widt = 400, height = 400)
canvas.pack()

my_image = PhotoImage(file='ball.gif')
canvas.create_image(10, 20, anchor = NW, image = my_image)
canvas.create_image(10, 200, anchor = NW, image = my_image)
canvas.create_image(200, 20, anchor = NW, image = my_image)
canvas.create_image(200, 200, anchor = NW, image = my_image)
tk.mainloop()