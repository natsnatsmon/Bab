import http.client
import urllib.request
import json
from pprint import pprint
from PIL import Image

# 서버 연결
server = "api.neople.co.kr"
apiKey = "7U2KCB4WfpbyjuvPBbqsz1uOxm4Waddl"
dataList = []

def connectOpenAPIServer():
    global conn, server
    conn = http.client.HTTPSConnection(server)
    conn.set_debuglevel(1)

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






# 서버 접속
connectOpenAPIServer()

InitTopText()
InitServerListBox()
InitInputLabel()
InitSearchButton()
InitRenderText()

#print("서버를 입력하세요.")
#serverId = input()

#print("캐릭터 이름을 입력하세요.")
#characterName = input()