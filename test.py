import http.client
from urllib import parse
import urllib.request
import json
from tkinter import *

# 서버 연결
server = "api.neople.co.kr"
apiKey = "7U2KCB4WfpbyjuvPBbqsz1uOxm4Waddl"

def connectOpenAPIServer():
    global conn, server
    conn = http.client.HTTPSConnection(server)
    conn.set_debuglevel(1)

# 캐릭터 이름, 서버로 정보 찾기
def getCharacterIdFromCharacterName(characterName):
    global server, conn, apiKey, serverId
    if conn == None:
        connectOpenAPIServer()

    encText = urllib.parse.quote(characterName)

    conn.request("GET", "/df/servers/" + serverId + "/characters?characterName=" + encText + "&apikey=" + apiKey)

    req = conn.getresponse()

    # 연결 상태 출력
    #print(req.status)

    if int(req.status) == 200:
        response_body = req.read()
        decode_response_body = response_body.decode('utf-8')
        print("\n----------------출력 내용-----------------\n")
        print(decode_response_body)

        json_response_body = json.loads(decode_response_body)
        dic_character_data = json_response_body['rows'][0]
        #        print(type(json_response_body))
        print(dic_character_data['characterName'])

    else:
        print("OpenAPI request has been failed!! please retry")
        return None


# 서버 접속

connectOpenAPIServer()


print("서버를 입력하세요.")
serverId = input()

print("캐릭터 이름을 입력하세요.")
characterName = input()

getCharacterIdFromCharacterName(characterName)