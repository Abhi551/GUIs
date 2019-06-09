try:
    from Tkinter import *
    from tkMessageBox import *
    import tkFileDialog 
    import os
    import sys
    import subprocess
    from subprocess import call
except ImportError :
    print ("Error while Importing modules.\nCheck if python 2 is used or not with all necessaries dependenciess")


## exception handling
## pass the arguments in second file before running
## use entry widgets to get the text in dialog box
## if any file not selected throught exception or message 


class Example(Frame):

    #4. constructor of the class, with window as argument
    def __init__(self, parent):
        Frame.__init__(self, parent)

        #5. making the window accesible to other functions
        self.parent = parent        
        self.initUI()
        
    def onOpen(self):

        #6. to read different types of file give argument here 
        ftypes = [('all files' , '*')]

        # dialog box to open files
        dlg = tkFileDialog.Open(self, filetypes = ftypes)
        # file_name stored
        fl_name = dlg.show()
        
        #7. to return the output
        ## subprocess.call(['./abc.py', arg1, arg2])
        '''
        call(["python", str(fl_name) ,  str(2),str(6)])
        '''


        label = Label(self.parent, text="File Location",font=12 , fg = 'red' , borderwidth =1 )
        label.pack(fill = X)
        label.place(relx=0.5, rely = 0.28, anchor = N ,height=30, width=150)
        
        #8. display the file path as box
        text = Text(self.parent, height=8, width=25)
        text.pack(fill = X)
        text.place(relx=0.5, rely = 0.35, anchor =N , height=100, width=500)

        self.fl_name = fl_name

        
        if fl_name != '':
            text.insert('1.0', fl_name)
            showinfo("message","file found")
        elif fl_name == '':
            showinfo("message","no file selected")            
            

        

    def start_program(self):
        
        #9. to print the final answer by the another program
        try:
            'the file that is to be executed is specified, with argument of file_name '
            'that is returned when a file selected by drop down menu'
    
            return_value = subprocess.check_output([sys.executable, "add.py" , self.fl_name])
            #10. printing the output of file executed , in this file
            self.return_value = return_value
        
            if "file executed" in return_value:
                showinfo("message","file is succesfully operated")

            print ("return _value")
            print(return_value)
        except :
            ## insert a new message box here 
            showinfo("Error", "File not selected")
        
        
    def initUI(self):

        ## title of the window
        try:
            self.parent.title("Open Files")
            self.pack(fill=BOTH, expand=1)

            ## adding the buttons
            #self.button1 = Button(self.parent, text="button1", width=15, height=2, command=self.func).place(x=0, y=0)
            self.button1 = Button(self.parent , text = "Click Here to Open File" , command = self.onOpen)
            self.button1.place(relx=0.5, rely = 0.03, anchor =N , height=30, width=150)
        
        
            self.button3 = Button(text='Start', command = self.start_program)
            self.button3.place(relx=0.5, rely = 0.17, anchor =N, height=30, width=150)
        

            ## Text, in built class of Tkinter
            self.txt = Text(self)
            self.txt.pack(side= "bottom" ,fill=BOTH, expand=1)
        except :
           print ("Buttons not executed")


def main():

    #1. intiating the window of GUsI
    window = Tk()
    ex = Example(window)
    
    #2. defining the geometry of window
    ## geometry >> x*y defines shape , + defines the location of window
    window.geometry("500x350+200+200")
    window.mainloop()  


if __name__ == '__main__':
    main()  
