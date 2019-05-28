from Tkinter import *

## Apart from pack there is another layou called,
## grid layout and write in GUIs
window = Tk()

window_label1 =  Label(window , text = 'Name' , fg = 'green' , bg = 'black')
entry1 = Entry(window)

window_label2 = Label(window , text = 'Roll No' , fg = 'green' , bg = 'black')
entry2 = Entry(window)

## placing the window_labels and entries using grid
window_label1.grid(row = 0 , column = 0)
window_label2.grid(row = 1 , column = 0)
entry1.grid(row = 0 , column = 1)
entry2.grid(row = 1 , column = 1)
window.mainloop()