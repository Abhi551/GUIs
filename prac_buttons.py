from Tkinter import *

## creating 
window = Tk()

def f1(event):
	print ("button1")

def f2(event):
	print ("button2")

def f3(event):
	print ("button3")

## creating the frame or space where the buttons while show the results on action
frame = Frame(window , width = 100 , height = 100)

## binding the buttons on the frame
frame.bind("<Button-1>",f1)
frame.bind("<Button-2>",f2)
frame.bind("<Button-3>",f3)
frame.grid()
window_label = Label(window , text = "buttons")
window_label.grid(row = 0 , columnspan = 2)
window.mainloop()