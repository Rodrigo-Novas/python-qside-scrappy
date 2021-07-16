import tkinter as tk
from tkinter import messagebox
from robot import create_block_hola, create_block_medio, create_block_chau, printer



class Mainframe(tk.Frame):
    # Mainframe contains the widgets
    # More advanced programs may have multiple frames
    # or possibly a grid of subframes
    
    def __init__(self,master,*args,**kwargs):
        # *args packs positional arguments into tuple args
        #  **kwargs packs keyword arguments into dict kwargs
        
        # initialise base class
        tk.Frame.__init__(self,master,*args,**kwargs)
        # in this case the * an ** operators unpack the parameters
        
        # put your widgets here
        #self.counter_message = tk.IntVar()
        tk.Label(self,textvariable = "Prueba calyx ejecutable v1").grid(row = 0,column = 0)
        tk.Button(self,text ="Mensaje",command = self.do_mensaje).grid(row = 1,column = 0)

    def do_mensaje(self):
        messagebox.showinfo(message="Hola mundo", title="Calyx prueba")
    
class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
               
        # set the title bar text
        self.title('Counter Demo')
        # Make sure app window is big enough to show title 
        self.geometry('300x100')
      
        # create and pack a Mainframe window
        Mainframe(self).pack()
        
        # now start
        self.mainloop()
                    
# create an App object
# it will run itself
App()