import tkinter as tk
from tkinter import messagebox
from robot import create_block_hola,create_block_medio,create_block_chau,printer
class Mainframe(tk.Frame):
 def __init__(self,master,*args,**kwargs):
  tk.Frame.__init__(self,master,*args,**kwargs)
  tk.Label(self,textvariable="Prueba calyx ejecutable v1").grid(row=0,column=0)
  tk.Button(self,text="Mensaje",command=self.do_mensaje).grid(row=1,column=0)
 def do_mensaje(self):
  messagebox.showinfo(message="Hola mundo",title="Calyx prueba")
class App(tk.Tk):
 def __init__(self):
  tk.Tk.__init__(self)
  self.title('Counter Demo')
  self.geometry('300x100')
  Mainframe(self).pack()
  self.mainloop()
App()
# Created by pyminifier (https://github.com/liftoff/pyminifier)
