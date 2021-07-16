import tkinter as tk
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
        self.counter_message = tk.IntVar()
        tk.Label(self,textvariable = self.counter_message).grid(row = 0,column = 0)
        tk.Button(self,text ="Start",command = self.do_start).grid(row = 1,column = 0)
        tk.Button(self,text ="Stop",command = self.do_stop).grid(row = 2,column = 0)
        
        self.count = 0
        self.delay = 100
        self.max_count = 100
        self.stop_count = False

    def director(self):
        """
        director function to manage functions
        :param texto: the texto to write
        :returns: None
        """
        if self.stop_count:
            return

        printer()

    
    def do_start(self):
        # called when start button pressed
        self.stop_count = False
        self.count = 0
        self.counter_message.set(self.count)
        self.after(self.delay,self.director())
        
    def do_stop(self):
        # called when stop button pressed
        self.stop_count = True
    
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