import http.client
import urllib.request
import json
from tkinter import *
from tkinter import font
import tkinter.messagebox
import characterWindow
import pickle
from collections import OrderedDict

server = "api.neople.co.kr"
apiKey = "7U2KCB4WfpbyjuvPBbqsz1uOxm4Waddl"

servers = [
    ("카인", "cain", 0, 0), ("안톤", "anton", 1, 0), ("시로코", "siroco", 2, 0), ("디레지에", "diregie", 3, 0),
    ("힐더", "hilder", 0, 2), ("바칼", "bakal", 1, 2), ("프레이", "prey", 2, 2), ("카시야스", "casillas", 3, 2)
]

servers_dict = { "cain" : "카인", "anton" : "안톤", "siroco" : "시로코", "diregie" : "디레지에",
                 "hilder" : "힐더", "bakal" : "바칼", "prey" : "프레이", "casillas" : "카시야스" }

def connectOpenAPIServer():
    global conn, server
    conn = http.client.HTTPSConnection(server)
    conn.set_debuglevel(1)

def raise_frame(frame):
    frame.tkraise()

def inin_auctionFrame():
    global frameAuction, itemEntry, tmpFont, itemData, itemlb, itemnum
    serverInputLabel = Label(frameAuction, text="아이템 이름", font = tmpFont)
    serverInputLabel.place(x=10 + 20, y=20)

    itemEntry = Entry(frameAuction, font=tmpFont, width=20)
    itemEntry.place(x=100 + 20, y=20)

    searchButton = Button(frameAuction, text = "검색", font = tmpFont, command = search_item)
    searchButton.place(x=250 + 20, y=16)

    r = open('item.json', mode="r", encoding="utf-8").read()
    itemData = json.loads(r)

    itemlb = Listbox(frameAuction, selectmode='extended', height=3)

    itemnum = 0

    for d in itemData:
        itemlb.insert(0, d)
        itemnum += 1
    itemlb.pack()
    itemlb.place(x = 100 + 20, y = 50)

    searchButton = Button(frameAuction, text="저장", font=tmpFont, command=save_item)
    searchButton.place(x=250 + 20, y=46 + 15)

    itemlb.bind('<<ListboxSelect>>', select_item)

    serverInputLabel = Label(frameAuction, text="즐겨찾기", font=tmpFont)
    serverInputLabel.place(x=10 + 20, y=50 + 15)

def save_item():
    global itemData, itemlb, itemnum
    itemName = itemEntry.get()
    if itemnum is 5:
        itemnum = 0
    itemData[itemnum] = itemName
    itemnum += 1
    with open('item.json', 'w', encoding="utf-8") as make_file:
        json.dump(itemData, make_file, ensure_ascii=False, indent="\t")
    itemlb.delete(0, END)
    for d in itemData:
        itemlb.insert(0, d)

def select_item(evt):
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    print ('You selected item %d: "%s"' % (index, value))
    itemEntry.delete(0, END)
    itemEntry.insert(INSERT, str(value))

def search_item():
    global itemEntry
    itemName = itemEntry.get()
    if itemName is '':
        tkinter.messagebox.showerror("DnF in", "아이템 이름을 입력해주세요")
    else:
        import auctionWindow
        auctionWindow.a_init_Window(itemName)
        auctionWindow.auctionWindow.mainloop()

def init_CharacterFrame():
    global selectedServer, tmpFont
    tmpFont = font.Font(window, size=10, weight='bold', family='Consolas')

    # 서버 선택 버튼
    serverInputLabel = Label(frameCharacter, text="서버", font = tmpFont)
    serverInputLabel.place(x=10, y=12)

    global selectedServer
    selectedServer = StringVar()
    selectedServer.set(None)

    for text, select, w, h in servers:
        serverRButton = Radiobutton(frameCharacter, text=text, font=tmpFont,
                                    value=select, variable=selectedServer)
        serverRButton.place(x=50 + (70 * w), y=10 + (15 * h))

    # 닉네임 입력 창
    serverInputLabel = Label(frameCharacter, text="닉네임", font = tmpFont)
    serverInputLabel.place(x=10, y=80)

    global characterEntry
    tmpFont = font.Font(frameCharacter, size=10, weight='bold', family='Consolas')
    characterEntry = Entry(frameCharacter, font=tmpFont, width=20)
    characterEntry.place(x=90, y=80)

    # 검색 버튼
    searchButton = Button(frameCharacter, text = "검색", font = tmpFont, command = command_CharacterSearch)
    searchButton.place(x=250, y=80)

    # 즐겨찾기 등록 버튼
    searchButton = Button(frameCharacter, text = "저장", font = tmpFont, command = command_CharacterBookmark)
    searchButton.place(x=300, y=80)

    # 즐겨찾기 리스트
    serverInputLabel = Label(frameCharacter, text="즐겨찾기", font=tmpFont)
    serverInputLabel.place(x=10, y=120)

    global characterData, characterNum, characterBookmarkListBox

    r = open('bookmark_character.json', mode="r", encoding="utf-8").read()

    characterData = json.loads(r)

    characterBookmarkListBox = Listbox(frameCharacter, font=tmpFont, selectmode = 'extended', width=35, height=3)
    characterNum = 0

    print(characterData)
    for d in characterData:
        characterBookmarkListBox.insert(characterNum, characterData[str(characterNum)]['server'] + " " +
                                        characterData[str(characterNum)]['characterName'] )
        characterNum += 1
    characterBookmarkListBox.pack()
    characterBookmarkListBox.place(x = 90, y = 120)

    characterBookmarkListBox.bind('<<ListboxSelect>>', select_character)

def select_character(evt):
    global characterData, selectedServer
    r = open('item.json', mode="r", encoding="utf-8").read()

    w = evt.widget
    index = int(w.curselection()[0])
    serverId = characterData[str(index)]['serverId']
    characterName = characterData[str(index)]['characterName']

    print ('You selected character %d: "%s" "%s"' % (index, serverId, characterName))
    characterEntry.delete(0, END)
    characterEntry.insert(INSERT, characterName)
    selectedServer.set(serverId)

def command_CharacterSearch():
    global selectedServer, characterEntry
    serverId = selectedServer.get()
    characterName = characterEntry.get()

    if server == 'None' :
        tkinter.messagebox.showerror("DnF in", "서버를 선택해주세요")
    elif characterName == '' :
        tkinter.messagebox.showerror("DnF in", "캐릭터 닉네임을 입력해주세요")
    else :
        if getCharacterIdFromCharacterName(serverId, characterName) == None:
            pass
        else :
            characterWindow.init_Ui(serverId, characterId)
            characterWindow.run_CharacterWindow()

# 캐릭터 이름, 서버로 정보 찾기
def getCharacterIdFromCharacterName(serverId, characterName):
    global server, conn, apiKey, characterId

    if conn == None:
        connectOpenAPIServer()

    encText = urllib.parse.quote(characterName)
    conn.request("GET", "/df/servers/" + serverId + "/characters?characterName=" + encText + "&apikey=" + apiKey)
    req = conn.getresponse()

    if int(req.status) == 200:
        response_body = req.read()
        decode_response_body = response_body.decode('utf-8')
        json_response_body = json.loads(decode_response_body)
        if not json_response_body['rows']:
            tkinter.messagebox.showerror("DnF in", "게임 내에 캐릭터가 존재하지 않습니다.")
            return None
        dic_character_data = json_response_body['rows'][0]
        print(dic_character_data['characterName'], dic_character_data['level'], dic_character_data['characterId'])
        # characterId 추출
        characterId = dic_character_data['characterId']
        return characterId


    else :
        tkinter.messagebox.showerror("DnF in", "다시 시도해주세요.")
        return None

def saveCharacter(serverId, characterName):
    global characterData, characterNum

    if characterNum is 5:
        characterNum = 0

    characterData[characterNum] = {"server" : servers_dict[serverId], "serverId" : serverId,
                                   "characterName" : characterName}

    characterNum += 1
    with open('bookmark_character.json', 'w', encoding="utf-8") as make_file:
        json.dump(characterData, make_file, ensure_ascii=False, indent="\t")

    characterBookmarkListBox.delete(0, END)

    for d in characterData:
        characterBookmarkListBox.insert(0, d)


def command_CharacterBookmark():
    global selectedServer, characterEntry
    serverId = selectedServer.get()
    characterName = characterEntry.get()

    if server == 'None':
        tkinter.messagebox.showerror("DnF in", "서버를 선택해주세요")
    elif characterName == '':
        tkinter.messagebox.showerror("DnF in", "캐릭터 닉네임을 입력해주세요")
        #    elif :
    else:
        if getCharacterIdFromCharacterName(serverId, characterName) == None :
            pass
        else :
            saveCharacter(serverId, characterName)


def init_Frame():
    global window, frameCharacter, frameAuction, buttonToCharacter, buttonToAction

    tmpFont = font.Font(window, size=12, weight='bold', family='Consolas')

    frameCharacter = LabelFrame(window, text = "캐릭터",width = 400 - 40, height = 250 - 40, font = tmpFont)
    frameAuction = LabelFrame(window, text = "경매장", width = 400 - 40, height = 150, font = tmpFont)
    frameCharacter.place(x = 20, y = 100)
    frameAuction.place(x = 20, y = 330)
    frameCharacter.pack_propagate(0)
    frameAuction.pack_propagate(0)

    init_CharacterFrame()
    inin_auctionFrame()

def init_Window():
    global window
    window = Tk()
    window.geometry("400x550")
    window.title("DnF in")

    logo = PhotoImage(file = "logo.png")
    logoLabel = Label(image = logo)
    logoLabel.image = logo
    logoLabel.pack()
    logoLabel.place(x = 10, y = 20)

    develop_logo = PhotoImage(file = "develop_logo.png")
    develop_logoLabel = Label(image = develop_logo)
    develop_logoLabel.image = develop_logo
    develop_logoLabel.place(x = 90, y = 500)

    tmpFont = font.Font(window, size=20, weight='bold', family='Consolas')
    mainText = Label(window, font = tmpFont, text = "던파 in")
    mainText.pack()
    mainText.place(x=120, y = 45)


    init_Frame()

def init_Ui():
    connectOpenAPIServer()
    init_Window()

def run_Window():
    global window
    raise_frame(frameCharacter)
    window.mainloop()