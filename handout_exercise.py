import playsound
from playsound import *
import tkinter
from tkinter import *


def play():
    filename = 'dj shane new (55).mp3'   #file name assuming by default its in your folder
    wave_obj = playsound(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()  # Wait until sound has finished playing


win = Tk()
win.title = "Music player"


#Lables
lbl1 = Label(win, text="Press to play sound")
lbl1.pack()

#Button
b1 = Button(win, text="Play", command=play)
b1.pack()

win.geometry('500x500')
win.mainloop()
