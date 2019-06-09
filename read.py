from Tkinter import *
import tkFileDialog 
import os
import sys
import subprocess
from subprocess import call

## add buttons in the dialog box to select and execute the file
## the output should appear in dialog box
## exception handling
## pass the arguments in second file before running
## use entry widgets to get the text in dialog box

class Example(Frame):

    ## constructor of the class, with window as argument
    def __init__(self, parent):
        
        Frame.__init__(self, parent)   

        ## making the window accesible to other functions
        self.parent = parent        
        self.initUI()
        
    def onOpen(self):

        ## to read different types of file give argument here 
        ftypes = [('all files' , '*')]
        dlg = tkFileDialog.Open(self, filetypes = ftypes)
        fl_name = dlg.show()

        print (fl_name)
        ## to return the output
        'call the python file passed in the subprocess argument, with additinal argument required to be passed'
        
        ## subprocess.call(['./abc.py', arg1, arg2])
    
        call(["python", str(fl_name)])

        ## to print the final answer by the another program
        ## file to be executed is passed in check_output
        return_value = subprocess.check_output([sys.executable, "add.py" ,str("4"), str("8"), fl_name])

        print (return_value)
        if fl_name != '':
            ## file can be displayed here 
            self.txt.insert(END,str(fl_name))
        else :
            self.txt.insert(END,"program not evaluated")


    def initUI(self):

        ## title of the window
        self.parent.title("File dialog")
        self.pack(fill=BOTH, expand=1)

        ## adding the buttons
        #self.button1 = Button(self.parent, text="button1", width=15, height=2, command=self.func).place(x=0, y=0)
        self.button1 = Button(self.parent , text = "Select File" , command = self.onOpen)
        #self.button1.grid(sticky = N)
        self.button1.pack() 
        self.button1.place(relx=0.5, rely=.95, anchor =CENTER, height=50, width=50)

        #self.button1.place(x=5, y=5, width=-10, height=-10)
        
        
        ## adding the menubar
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Open", command=self.onOpen)
        menubar.add_cascade(label="File", menu=fileMenu)        
    

        ## Text, in built class of Tkinter
        self.txt = Text(self)
        self.txt.pack(side= "bottom" ,fill=BOTH, expand=1)


def main():

    ## intiating the window of GUsI
    window = Tk()
    ex = Example(window)
    ## defining the geometry of window
    ## geometry >> x*y defines shape , + defines the location of window
    window.geometry("350x350+300+300")
    window.mainloop()  


if __name__ == '__main__':
    main()  
