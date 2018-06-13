from tkinter import *
from tkinter import font
import tkinter.messagebox

def init_Frame():
    global characterWindow, frameInfo, frameStatus, frameEquipment

    tmpFont = font.Font(characterWindow, size=12, weight='bold', family='Consolas')

    frameInfo = LabelFrame(characterWindow, width =400 - 40, height =250 - 40)
    frameStatus = LabelFrame(characterWindow, text ="능력치", width =400 - 40, height =250 - 40, font = tmpFont)
    frameEquipment = LabelFrame(characterWindow, text ="장착 장비", width =400 - 40, height =250 - 40, font = tmpFont)

    frameInfo.place(x = 20, y = 20)
    frameStatus.place(x=20, y=100)
    frameEquipment.place(x=20, y=100)

    frameInfo.pack_propagate(0)
    frameStatus.pack_propagate(0)
    frameEquipment.pack_propagate(0)

    #init_InfoFrame()
    #init_StatusFrame()
    #init_Equipment()

def init_CharacterWindow():
    global characterWindow

    characterWindow = Toplevel()
    characterWindow.geometry("600x400")
    characterWindow.title("DnF in")

    tmpFont = font.Font(characterWindow, size=20, weight ='bold', family ='Consolas')
    mainText = Label(characterWindow, font = tmpFont, text ="던파 in")
    mainText.pack()
    mainText.place(x=20, y = 20)

    init_Frame()

def init_CharacterUi():
    #connectOpenAPIServer()
    init_CharacterWindow()

def run_CharacterWindow():
    init_CharacterUi()

    global characterWindow
#    raise_frame(frameCharacter)
    characterWindow.mainloop()

#        RenderText.insert(INSERT, "[캐릭터 이름] : ")
#        RenderText.insert(INSERT, dic_character_data['characterName'])
#        RenderText.insert(INSERT, "\n")
#        RenderText.insert(INSERT, "[레벨] : ")
#        RenderText.insert(INSERT, dic_character_data['level'])
#        RenderText.insert(INSERT, "\n")
#        RenderText.insert(INSERT, "[직업] : ")
#        RenderText.insert(INSERT, dic_character_data['jobName'])
#        RenderText.insert(INSERT, "\n")
#        RenderText.insert(INSERT, "[전직] : ")
#        RenderText.insert(INSERT, dic_character_data['jobGrowName'])
#        RenderText.insert(INSERT, "\n")