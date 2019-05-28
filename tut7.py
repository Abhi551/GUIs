from Tkinter import *

## binding buttons of mouse to specified functions 

window = Tk()

def f(event):
	print ("1st event")

def f2(event):
	print ("2nd event")

def f3(event):
	print ('3rd event')


window_label = Label(text = "Mouse Clicks")
window_label.grid(row = 0 , columnspan = 2)

frame = Frame(window , width = 300 , height = 250)
frame.bind("<Button-1>",f)
frame.bind("<Button-2>",f2)
frame.bind("<Button-3>",f3)
frame.grid()
window.mainloop()



