from tkinter import *
from tkinter import font

def InitTopText():
    tmpFont = font.Font(client_window, size=20, weight = 'bold', family = 'Consolas')
    mainText = Label(client_window, font = tmpFont, text = "던파 in")
    mainText.pack()
    mainText.place(x=20, y = 20)

# tkinter
client_window = Tk()
client_window.geometry("400x600")

InitTopText()

fr_character = LabelFrame(client_window, text='Character', width=49, height=27)
fr_character.place(x = 50, y = 150)
fr_character.pack(expand=YES, pady=100 )

fr_item = LabelFrame(client_window, text='Item', width=49, height=27)
fr_item.place(x = 50, y = 350)
fr_item.pack(expand=YES, pady=100 )


client_window.mainloop()