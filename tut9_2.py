## editing menus and sub_menus

from Tkinter import *

window = Tk()

window_label = Label(window , text = "drop_down_menu" )

## main menus
main_menu1 = Menu(window)
## use to access objects attributes after intialisation

window.config(menu = main_menu1)

window.mainloop()