import http.client
import urllib.request
import json
from tkinter import *
from tkinter import font
from PIL import ImageTk
from PIL import Image
from io import BytesIO
import tkinter.messagebox

server = "api.neople.co.kr"
apiKey = "7U2KCB4WfpbyjuvPBbqsz1uOxm4Waddl"
global serverId, characterId

def connectOpenAPIServer():
    global conn, server
    conn = http.client.HTTPSConnection(server)
    conn.set_debuglevel(1)

def init_Image():
    global window, characterImage, characterImageLabel, frameInfo
    url = "https://img-api.neople.co.kr/df/servers/" + serverId + "/characters/" + characterId + "?zoom=2"

    with urllib.request.urlopen(url) as u:
        raw_data = u.read()

    im = Image.open(BytesIO(raw_data))
    im = im.resize((240, 276), Image.ANTIALIAS)
    characterImage = ImageTk.PhotoImage(im)
    characterImageLabel = Label(window, image = characterImage, width = 200, height= 230)
    characterImageLabel.place(x=40, y=-20)
    characterImageLabel.pack_propagate(0)

def init_Frame():
    global window, frameInfo, frameStatus, frameEquipment

    tmpFont = font.Font(window, size=12, weight='bold', family='Consolas')

    frameInfo = LabelFrame(window, width = 250, height = 150)
    frameStatus = LabelFrame(window, text ="능력치", width = 290, height = 170, font = tmpFont)
    frameEquipment = LabelFrame(window, text ="장착 장비", width = 290, height = 170, font = tmpFont)

    frameInfo.place(x = 20, y = 230)
    frameStatus.place(x = 290, y=20)
    frameEquipment.place(x=290, y=210)

    frameInfo.pack_propagate(0)
    frameStatus.pack_propagate(0)
    frameEquipment.pack_propagate(0)

    init_InfoFrame()
    init_StatusFrame()
    init_Equipment()

def init_InfoFrame():
    global server, conn, apiKey
    print(serverId, characterId)

    if conn == None:
        connectOpenAPIServer()

    conn.request("GET", "/df/servers/"+serverId+"/characters/" + characterId +"?apikey=" + apiKey)
    req = conn.getresponse()

    if int(req.status) == 200:
        response_body = req.read()
        decode_response_body = response_body.decode('utf-8')
        json_response_body = json.loads(decode_response_body)
        dic_info_data = json_response_body

        tmpFont = font.Font(frameInfo, size=25, weight='bold', family='Consolas')
        characterNameText = Label(frameInfo, font=tmpFont, text=dic_info_data['characterName'],
                                  pady = 20, justify = CENTER)
        characterNameText.pack()

        levelJobText = "Lv. " + str(dic_info_data['level']) + " | " + dic_info_data['jobGrowName']
        tmpFont = font.Font(frameInfo, size=15, family='Consolas')
        characterLevelJobText = Label(frameInfo, font=tmpFont, text=levelJobText,
                                  pady = 0, justify = CENTER)
        characterLevelJobText.pack()

        tmpFont = font.Font(frameInfo, size=15, family='Consolas')
        characterGuildNameText = Label(frameInfo, font=tmpFont, text=dic_info_data['guildName'], pady = 0, justify = CENTER)
        characterGuildNameText.pack()

    else:
        tkinter.messagebox.showerror("DnF in", "다시 시도해주세요.")
        return None

def init_StatusFrame():
    global server, conn, apiKey
    print(serverId, characterId)

    if conn == None:
        connectOpenAPIServer()

    conn.request("GET", "/df/servers/"+serverId+"/characters/" + characterId +"?apikey=" + apiKey)
    req = conn.getresponse()

    if int(req.status) == 200:
        response_body = req.read()
        print("\n---------------여기까지출력됨---------------\n")
        decode_response_body = response_body.decode('utf-8')
        json_response_body = json.loads(decode_response_body)
        dic_info_data = json_response_body

        tmpFont = font.Font(frameInfo, size=25, weight='bold', family='Consolas')
        characterNameText = Label(frameInfo, font=tmpFont, text=dic_info_data['characterName'],
                                  pady = 20, justify = CENTER)
        characterNameText.pack()

        levelJobText = "Lv. " + str(dic_info_data['level']) + " | " + dic_info_data['jobGrowName']
        tmpFont = font.Font(frameInfo, size=15, family='Consolas')
        characterLevelJobText = Label(frameInfo, font=tmpFont, text=levelJobText,
                                  pady = 0, justify = CENTER)
        characterLevelJobText.pack()

        tmpFont = font.Font(frameInfo, size=15, family='Consolas')
        characterGuildNameText = Label(frameInfo, font=tmpFont, text=dic_info_data['guildName'], pady = 0, justify = CENTER)
        characterGuildNameText.pack()

    else:
        tkinter.messagebox.showerror("DnF in", "다시 시도해주세요.")
        return None

def init_Equipment():
    global server, conn, apiKey
    print(serverId, characterId)

    if conn == None:
        connectOpenAPIServer()

    conn.request("GET", "/df/servers/"+serverId+"/characters/" + characterId +"/equip/equipment?apikey=" + apiKey)
    req = conn.getresponse()

    if int(req.status) == 200:
        response_body = req.read()
        print("\n---------------여기까지출력됨---------------\n")
        decode_response_body = response_body.decode('utf-8')
        json_response_body = json.loads(decode_response_body)
        dic_info_data = json_response_body['equipment']

        print(dic_info_data[0]['slotName'], dic_info_data[1]['slotName'])
#        itemList = []
#        for i in dic_info_data:
#            slotItemName = dic_info_data[i]['soltName'] + dic_info_data[i]['itemName']
#            itemList.append(slotItemName)

#        tmpFont = font.Font(frameEquipment, size=25, weight='bold', family='Consolas')
#        characterNameText = Label(frameInfo, font=tmpFont, text=itemList[0],
#                                  pady = 20, justify = CENTER)
#        characterNameText.pack()

    else:
        tkinter.messagebox.showerror("DnF in", "다시 시도해주세요.")
        return None

def init_Window():
    global window

    window = Toplevel()
    window.geometry("600x400")
    window.title("DnF in")

    init_Frame()
    init_Image()

def init_Ui(sId, cId):
    global window, serverId, characterId
    serverId = sId
    characterId = cId
    connectOpenAPIServer()
    init_Window()

def run_CharacterWindow():
    window.mainloop()

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