from Tkinter import *

window = Tk()

def func(event):
	print ('Binded')

def func2(event):
	print('2nd')
window_label = Label(window , text = "Binding the mouse button" , fg = 'green')
window_label.grid(row = 0)

button1 = Button(window , text = "button1")
button1.bind('<Button-1>' , func)


button1.grid(row=1 , column = 0)


window.mainloop()

