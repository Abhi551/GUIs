from Tkinter import *

win1 = Tk()

win1_label = Label(win1 , text = 'Abhishek')
win1_label.pack()

## adding buttons
frame1 = Frame(win1)
frame1.pack(side = TOP)


frame2 = Frame(win1)
frame2.pack(side = BOTTOM)

b1 = Button(frame1 , text = 'Button1')
b1.pack(side = RIGHT)

b2 = Button(frame2 , text = 'Button2')
b2.pack(side = LEFT)
win1.mainloop()
