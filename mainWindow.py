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

def raise_frame(frame):
    frame.tkraise()

def init_Frame():
    global window, frameCharacter, frameAuction, buttonToCharacter, buttonToAction
    frameCharacter = LabelFrame(window, text = "캐릭터", width = 400 - 40, height = 250 - 40)
    frameAuction = LabelFrame(window, text = "경매장", width = 400 - 40, height = 250 - 40)
    frameCharacter.place(x = 20, y = 120)
    frameAuction.place(x = 20, y = 370)

    Label(frameCharacter, text = '캐릭터').pack()
    Label(frameAuction, text = '경매장').pack()

    serverInputLabel = Label(frameCharacter, text="서버")
    serverInputLabel.place(x=50, y=100)

    #    ServerBoxScroll = Scrollbar(DnF_In_window)
    #    ServerBoxScroll.pack()
    #    ServerBoxScroll.place(x = 200, y = 100)

    tmpFont = font.Font(frameCharacter, size=10, weight='bold', family='Consolas')
    ServerListBox = Listbox(frameCharacter, font=tmpFont, activestyle='none', width=10, height=4)

    ServerListBox.insert(1, "카인")
    ServerListBox.insert(2, "디레지에")
    ServerListBox.insert(3, "시로코")
    ServerListBox.insert(4, "프레이")
    ServerListBox.insert(5, "카시야스")
    ServerListBox.insert(6, "힐더")
    ServerListBox.insert(7, "안톤")
    ServerListBox.insert(8, "바칼")
    ServerListBox.place(x=100, y=100)
    ServerListBox.pack()

    characterInputLabel = Label(frameCharacter, text="닉네임")
    characterInputLabel.place(x=50, y=200)
    characterInputLabel.pack()


def init_Window():
    global window
    window = Tk()
    window.geometry("400x600")

    tmpFont = font.Font(window, size=20, weight = 'bold', family = 'Consolas')
    mainText = Label(window, font = tmpFont, text = "던파 in")
    mainText.pack()
    mainText.place(x=20, y = 20)

    init_Frame()

def init_Ui():
    connectOpenAPIServer()
    init_Window()

def run_Window():
    global window
    raise_frame(frameCharacter)
    window.mainloop()

init_Ui()
run_Window()