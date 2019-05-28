from Tkinter import *

## binding functions to the layout,
## and connecting the mouse button with them

window =   Tk()
def function():
	print ('Abhishek');


window_label1 = Label(window , text = 'Running a function' , fg = 'green')
window_label2 = Label(window , text = 'Name' , fg = 'green')

button1 = Button(window , text = "Print Name" , command =function)
button1.grid(row = 2 , columnspan = 2)

entry1 = Entry(window)

window_label1.grid(row = 0 ,columnspan = 2)
window_label2.grid(row = 1 , sticky = W) 	 	
entry1.grid(row = 1 , column = 1)


window.mainloop()

