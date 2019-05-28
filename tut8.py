from Tkinter import *



## using classes to create the buttons that will help in perform the different actions 
class Buttons_class:

	def __init__(self ,window_passed):
		## as the object is instancited create the frame on the window
		frame =  Frame(window_passed , width = 250 , height = 250)
		

		## create the buttons on GUI
		self.b1 = Button(frame , text = "button1" , command = self.func1)
		self.b1.grid(sticky = W)


		self.b2 = Button(frame , text = "button2" , command = self.func2)
		self.b2.grid(sticky = W)

		self.quitButton = Button(frame , text = "Quit" , command = frame.quit)
		self.quitButton.grid()

		frame.grid()

	def func1(self):
		print ("this is my button")

	def func2(self):
		print ("this is my button2")


window = Tk()

window_label =  Label(window , text = "classes in GUI" , fg = 'green')
window_label.grid(row = 0 , columnspan = 3)

b = Buttons_class(window)
window.mainloop()