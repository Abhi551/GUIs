## orgaizing the layout and displaying the widgets 
from Tkinter import *

win = Tk()


## for labeling the display window with text
label_win = Label(win , text = 'Second Window')

## top window
top_win = Frame(win)
top_win.pack()

## botton window
bot_win = Frame(win)
bot_win.pack(side = BOTTOM)

## adding the buttons 
b1 = Button(top_win, text = 'Button1' , fg = 'red')
b2 = Button(top_win, text = 'Button2' , fg = 'blue')
b3 = Button(top_win, text = 'Button3' , fg = 'black')
b4 = Button(bot_win, text = 'Button4' , fg = 'green')

b1.pack(side = LEFT)
b2.pack(side = LEFT)
b3.pack(side = LEFT)
b4.pack()

label_win.pack()
## run infinte loop
win.mainloop()