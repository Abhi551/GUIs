## editing menus and sub_menus
from Tkinter import *

window = Tk()
window_label = Label(window , text = "drop_down_menu" )

def fun1():
	print("sub_menu1")

def fun2():
	print("sub_menu2")

## main menu1

main_menu1 = Menu(window)
## use to access objects attributes after intialisation

window.config(menu = main_menu1)

sub_menu1 = Menu(main_menu1)

## creating sub menu for the main menu
main_menu1.add_cascade(label = "main_menu1" , menu = sub_menu1)

## creating the commands for each sub menus
## creating multiple sub-menus for the main_menu1
sub_menu1.add_command(label = "sub_menu1" , command = fun1 )
sub_menu1.add_command(label = "sub_menu2" , command = fun2 )
'''
sub_menu1.add_separator()

main_menu2 = Menu(main_menu1)
window.config(menu = main_menu2)

## each time new object is instanciated during the call of Menu()
sub_menu1 = Menu(main_menu2)
main_menu1.add_cascade(label = "main_menu1" , menu = sub_menu1)

sub_menu1.add_command(label = 'sub_menu1', command = fun1)
sub_menu1.add_command(label = 'sub_menu2', command = fun2)

sub_menu1.add_separator()
## creating other main menus with added sub menus for them

'''
main_menu3 = Menu(window)

window.config(menu = main_menu3)

## adding the sub menu to main menu
sub_menu1 = Menu(main_menu3)

main_menu3.add_cascade(label = 'sub_menu1' , menu = sub_menu1)

sub_menu1.add_command(label = "sub_menu1" , command = fun1)
sub_menu1.add_command(label = "sub_menu2" , command = fun2)
sub_menu1.add_separator()

window.mainloop()