import http.client
import urllib.request
import json
from tkinter import *
from tkinter import font
import tkinter.messagebox
import characterWindow

server = "api.neople.co.kr"
apiKey = "7U2KCB4WfpbyjuvPBbqsz1uOxm4Waddl"

servers = [
    ("카인", "cain", 0, 0), ("안톤", "anton", 1, 0), ("시로코", "siroco", 2, 0), ("디레지에", "diregie", 3, 0),
    ("힐더", "hilder", 0, 2), ("바칼", "bakal", 1, 2), ("프레이", "prey", 2, 2), ("카시야스", "casillas", 3, 2)
]

def connectOpenAPIServer():
    global conn, server
    conn = http.client.HTTPSConnection(server)
    conn.set_debuglevel(1)

def raise_frame(frame):
    frame.tkraise()

def inin_auctionFrame():
    global frameAuction, itemEntry, tmpFont
    serverInputLabel = Label(frameAuction, text="아이템 이름", font = tmpFont)
    serverInputLabel.place(x=10 + 20, y=20)

    itemEntry = Entry(frameAuction, font=tmpFont, width=20)
    itemEntry.place(x=100 + 20, y=20)

    searchButton = Button(frameAuction, text = "검색", font = tmpFont, command = search_item)
    searchButton.place(x=250 + 20, y=16)

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

    selectedServer = StringVar()
    selectedServer.set(None)

    for text, select, w, h in servers:
        serverRButton = Radiobutton(frameCharacter, text=text, font=tmpFont,
                                    value=select, variable=selectedServer)
        serverRButton.place(x=50 + (70 * w), y=10 + (10 * h))

    # 닉네임 입력 창
    serverInputLabel = Label(frameCharacter, text="닉네임", font = tmpFont)
    serverInputLabel.place(x=10, y=60)

    global characterEntry
    tmpFont = font.Font(frameCharacter, size=10, weight='bold', family='Consolas')
    characterEntry = Entry(frameCharacter, font=tmpFont, width=15)
    characterEntry.place(x=70, y=60)

    # 검색 버튼
    searchButton = Button(frameCharacter, text = "검색", font = tmpFont, command = command_CharacterSearch)
    searchButton.place(x=200, y=60)

    # 즐겨찾기 등록 버튼
    searchButton = Button(frameCharacter, text = "즐겨찾기 등록", font = tmpFont, command = command_CharacterBookmark)
    searchButton.place(x=250, y=60)

    # 즐겨찾기 리스트
    serverInputLabel = Label(frameCharacter, text="즐겨찾기", font=tmpFont)
    serverInputLabel.place(x=10, y=120)

def command_CharacterSearch():
    global selectedServer, characterEntry
    serverId = selectedServer.get()
    characterName = characterEntry.get()

    if server == 'None' :
        tkinter.messagebox.showerror("DnF in", "서버를 선택해주세요")
    elif characterName == '' :
        tkinter.messagebox.showerror("DnF in", "캐릭터 닉네임을 입력해주세요")
    else :
        getCharacterIdFromCharacterName(serverId, characterName)

# 캐릭터 이름, 서버로 정보 찾기
def getCharacterIdFromCharacterName(serverId, characterName):
    global server, conn, apiKey
    print(serverId, characterName)

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
        characterWindow.init_Ui(serverId, characterId)
        characterWindow.run_CharacterWindow()

    else :
        tkinter.messagebox.showerror("DnF in", "다시 시도해주세요.")
        return None

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
        print(server, characterName)
    pass

def init_Frame():
    global window, frameCharacter, frameAuction, buttonToCharacter, buttonToAction

    tmpFont = font.Font(window, size=12, weight='bold', family='Consolas')

    frameCharacter = LabelFrame(window, text = "캐릭터",width = 400 - 40, height = 250 - 40, font = tmpFont)
    frameAuction = LabelFrame(window, text = "경매장", width = 400 - 40, height = 250 - 40, font = tmpFont)
    frameCharacter.place(x = 20, y = 100)
    frameAuction.place(x = 20, y = 340)
    frameCharacter.pack_propagate(0)
    frameAuction.pack_propagate(0)

    init_CharacterFrame()
    inin_auctionFrame()

def init_Window():
    global window
    window = Tk()
    window.geometry("400x600")
    window.title("DnF in")

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