from Tkinter  import *

## creating drop down menu 
	
window = Tk()

def func1():
	print ("func1")


def func2():
	print ("func2")


def func3():
	print ("func3")
## creating a menu 
win_menu = Menu(window)
window.config(menu = win_menu)

## creating sub menus in menu
## i.e, cascading in Tkinter 

sub_menu = Menu(win_menu)
## creates widget or button with drop down functionality and we can add more submenu to "new" 
win_menu.add_cascade(label = "new", menu = sub_menu)

## we can write functions to the sub menus to operate 
sub_menu.add_command(label = "file" , command = func1)
sub_menu.add_command(label = "open" , command = func2)
sub_menu.add_command(label = "save" , command = func3)

window.mainloop()
