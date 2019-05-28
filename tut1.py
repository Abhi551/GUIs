from Tkinter import *

## constructor of class tkinter 
## empty screen
root = Tk()

## gives label on empty screen root
label = Label(root, text = "first, printing long places");

## statements window on screen
label.pack()

## runs infinite loop to window to appear continously
root.mainloop()