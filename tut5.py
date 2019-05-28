from Tkinter import *

window = Tk()

## text alignment on labels of the windows 
## N = north , S,E,W.
## check button in GUIs
## expanding the widgets

window_label1 = Label(window , text = 'Name' , fg = 'green')
window_label2 = Label(window , text = 'Roll Number' , fg = 'green')
window_label3 = Label(window , text = 'College' , fg =  'green')

entry1 = Entry(window)
entry2 = Entry(window)
entry3 = Entry(window)

window_label1.grid(row = 0 , column = 0 , sticky = E)
window_label2.grid(row = 1 , column = 0 , sticky = N)
window_label3.grid(row = 2 , column = 0 , sticky = W)
entry1.grid(row = 0 , column = 1)
entry2.grid(row = 1 , column = 1)  
entry3.grid(row = 2 , column = 1)

## checkbutton 
c = Checkbutton(window , text = 'Remember')
c.grid(columnspan = 2 , sticky = W)

window.mainloop()

