from tkinter import Tk, Button
from cancel_token import CancellationToken
from robot import director
token = CancellationToken()

tkinterO = Tk()
tkinterO.title("Control de mando")
tkinterO.geometry("350x250")
delay = 100 

def play_pause() -> None:
    """
    Play and pause a robot
    :param texto: the texto to write
    :returns: None
    """
    if button["text"] == "Play":
        button["text"] = "Pause"
        button["bg"] = "yellow"
        tkinterO.after(delay,director("Play"))
    else:
        button["text"] = "Play"
        button["bg"] = "green"
        tkinterO.after(delay,director("Pause"))




button = Button(tkinterO, text='Play', width=14,
                bg='green', fg='black', command=play_pause)
button.pack()

tkinterO.mainloop()
