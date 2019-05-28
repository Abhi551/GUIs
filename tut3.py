from Tkinter import *

## filtering widgets in GUI 
window = Tk()

window_label1 = Label(window , text = "tut3" , fg = 'green' , bg = 'black')
window_label1.pack()

window_label2 = Label(window, text = 'Second window' , fg = 'white' , bg = 'black')
window_label2.pack(fill = X)

window_label3 =  Label(window , text = 'Third window' , fg = 'blue' , bg = 'black')
window_label3.pack(side = LEFT,fill = Y)
window.mainloop()