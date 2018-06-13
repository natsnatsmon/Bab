from mainWindow import *

def init_CharacterWindowFrame():
    global characterWindow, frameCharacterInfo, frameCharacterStatus, frameCharacterEquipment

    tmpFont = font.Font(characterWindow, size=12, weight='bold', family='Consolas')

    frameCharacterInfo = LabelFrame(characterWindow, width =400 - 40, height =250 - 40)
    frameCharacterStatus = LabelFrame(characterWindow, text ="능력치", width =400 - 40, height =250 - 40, font = tmpFont)
    frameCharacterEquipment = LabelFrame(characterWindow, text ="장착 장비", width =400 - 40, height =250 - 40, font = tmpFont)

    frameCharacterInfo.place(x = 20, y = 20)
    frameCharacterStatus.place(x=20, y=100)
    frameCharacterEquipment.place(x=20, y=100)

    frameCharacterInfo.pack_propagate(0)
    frameCharacterStatus.pack_propagate(0)
    frameCharacterEquipment.pack_propagate(0)

    init_CharacterWindowFrame()

def init_CharacterWindow():
    global characterWindow
    characterWindow = Tk()
    characterWindow.geometry("400x600")
    characterWindow.title("DnF in")

    tmpFont = font.Font(characterWindow, size=20, weight ='bold', family ='Consolas')
    mainText = Label(characterWindow, font = tmpFont, text ="던파 in")
    mainText.pack()
    mainText.place(x=20, y = 20)

    init_Frame()

def init_CharacterUi():
    connectOpenAPIServer()
    init_CharacterWindow()

def run_CharacterWindow():
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