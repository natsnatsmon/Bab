from tkinter import *
from tkinter import font

def InitTopText():
    tmpFont = font.Font(DnF_In_window, size=20, weight = 'bold', family = 'Consolas')
    mainText = Label(DnF_In_window, font = tmpFont, text = "던파 in")
    mainText.pack()
    mainText.place(x=20, y = 20)

# tkinter
DnF_In_window = Tk()
DnF_In_window.geometry("400x600")

DnF_In_window.mainloop()