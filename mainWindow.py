import http.client
import urllib.request
import json
from tkinter import *
from tkinter import font

server = "api.neople.co.kr"
apiKey = "7U2KCB4WfpbyjuvPBbqsz1uOxm4Waddl"

def connectOpenAPIServer():
    global conn, server
    conn = http.client.HTTPSConnection(server)
    conn.set_debuglevel(1)

def init_Window():
    global window
    window = Tk()
    window.geometry("400x600")

    tmpFont = font.Font(window, size=20, weight = 'bold', family = 'Consolas')
    mainText = Label(window, font = tmpFont, text = "던파 in")
    mainText.pack()
    mainText.place(x=150, y = 20)

    init_Frame()

def init_Ui():
    connectOpenAPIServer()
    init_Window()

def raise_frame(frame):
    frame.tkraise()

def init_Frame():
    global window, frameCharacter, frameAction, buttonToCharacter, buttonToAction
    frameCharacter = LabelFrame(window, text = "캐릭터", width = 400 - 40, height = 250 - 40)
    frameAction = LabelFrame(window, text = "경매장", width = 400 - 40, height = 250 - 40)
    frameCharacter.place(x = 20, y = 120)
    frameAction.place(x = 20, y = 370)

    Label(frameCharacter, text = '캐릭터').pack()
    Label(frameAction, text = '경매장').pack()

def run_Window():
    global window
    raise_frame(frameCharacter)
    window.mainloop()

init_Ui()
run_Window()