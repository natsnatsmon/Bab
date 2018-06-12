from ui import *

dataList = []

def InitServerListBox() :
    global frameCharacter, ServerListBox
    serverInputLabel = Label(frameCharacter, text="서버")
    serverInputLabel.place(x=50, y=100)

    #    ServerBoxScroll = Scrollbar(frameCharacter)
#    ServerBoxScroll.pack()
#    ServerBoxScroll.place(x = 200, y = 100)

    tmpFont = font.Font(frameCharacter, size = 10, weight = 'bold', family = 'Consolas')
    ServerListBox = Listbox(frameCharacter, font = tmpFont, activestyle = 'none', width = 10, height = 4)

    ServerListBox.insert(1, "카인")
    ServerListBox.insert(2, "디레지에")
    ServerListBox.insert(3, "시로코")
    ServerListBox.insert(4, "프레이")
    ServerListBox.insert(5, "카시야스")
    ServerListBox.insert(6, "힐더")
    ServerListBox.insert(7, "안톤")
    ServerListBox.insert(8, "바칼")
    ServerListBox.pack()
    ServerListBox.place(x = 100, y = 100)

def InitInputLabel() :
    global frameCharacter
    characterInputLabel = Label(frameCharacter, text="닉네임")
    characterInputLabel.place(x=50, y=200)

    global characterEntry
    tmpFont = font.Font(frameCharacter, size=10, weight='bold', family='Consolas')
    characterEntry = Entry(frameCharacter, font=tmpFont, width=15)
    characterEntry.pack()
    characterEntry.place(x=100, y=200)

def InitSearchButton() :
    global frameCharacter
    tmpFont = font.Font(frameCharacter, size=10, weight='bold', family='Consolas')
    searchButton = Button(frameCharacter, font = tmpFont, text="검색", command = SearchButtonAction)
    searchButton.place(x=150, y=250)

def SearchButtonAction() :
    RenderText.configure(state = 'normal')
    RenderText.delete(0.0, END)

    getCharacterIdFromCharacterName()

    RenderText.configure(state='disabled')


def InitRenderText() :
    global RenderText, frameCharacter
#    RenderTextScrollbar = Scrollbar(frameCharacter)
#    RenderTextScrollbar.pack()
#    RenderTextScrollbar.place(x=375, y=200)
    tmpFont = font.Font(frameCharacter, size=10, family='Consolas')
    RenderText = Text(frameCharacter, font = tmpFont, width=49, height=27)
    RenderText.pack()
    RenderText.place(x=10, y=280)
#    RenderTextScrollbar.config(command=RenderText.yview)
#    RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)
    RenderText.configure(state='disabled')

# 캐릭터 이름, 서버로 정보 찾기
def getCharacterIdFromCharacterName():
    global server, conn, apiKey, serverId, characterName, ServerListBox
    if conn == None:
        connectOpenAPIServer()

    myServer = ServerListBox.curselection()[0]
    if myServer == 0:
        serverId = "cain"
    elif myServer == 1:
        serverId = "diregie"
    elif myServer == 2:
        serverId = "siroco"
    elif myServer == 3:
        serverId = "prey"
    elif myServer == 4:
        serverId = "casillas"
    elif myServer == 5:
        serverId = "hilder"
    elif myServer == 6:
        serverId = "anton"
    else :
        serverId = "bakal"

    characterName = characterEntry.get()
    encText = urllib.parse.quote(characterName)

    conn.request("GET", "/df/servers/" + serverId + "/characters?characterName=" + encText + "&apikey=" + apiKey)

    req = conn.getresponse()

    dataList.clear()

    # 연결 상태 출력
    #print(req.status)

    if int(req.status) == 200:
        response_body = req.read()
#        print(response_body, type(response_body))
        print("\n---------------여기까지출력됨---------------\n")
        decode_response_body = response_body.decode('utf-8')
#        print(decode_response_body)

#        print(type(decode_response_body))

        json_response_body = json.loads(decode_response_body)
        dic_character_data = json_response_body['rows'][0]
#        print(type(json_response_body))
        print(dic_character_data['characterName'])

        print("\n---------------여기까지출력됨---------------\n")

        RenderText.insert(INSERT, "[캐릭터 이름] : ")
        RenderText.insert(INSERT, dic_character_data['characterName'])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "[레벨] : ")
        RenderText.insert(INSERT, dic_character_data['level'])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "[직업] : ")
        RenderText.insert(INSERT, dic_character_data['jobName'])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "[전직] : ")
        RenderText.insert(INSERT, dic_character_data['jobGrowName'])
        RenderText.insert(INSERT, "\n")

    else:
        print("OpenAPI request has been failed!! please retry")
        return None

def init_Character():
    InitServerListBox()
    InitInputLabel()
    InitSearchButton()
    InitRenderText()