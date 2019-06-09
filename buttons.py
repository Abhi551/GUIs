from Tkinter import *


window = Tk()
window_label =  Label(window , text = "classes in GUI" , fg = 'green')
window_label.pack()


def func1():
    print ("this is my button")

def func2():
    print ("this is my button2")


text = Text(window)
text.insert(INSERT, "Hello.....")
text.insert(END, "Bye Bye.....")
text.pack()

text.tag_add("here", "1.0", "1.4")
text.tag_add("start", "1.8", "1.13")
text.tag_config("here", background="yellow", foreground="blue")
text.tag_config("start", background="black", foreground="green")


## buttons
b1 = Button(window , text = "button1" , command = func1)
b1.pack(side = "top" , fill = 'both', expand =1)


b2 = Button(window , text = "button2" , command = func2)
b2.pack( fill = 'both', expand = 1)


window.mainloop()
