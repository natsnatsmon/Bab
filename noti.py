import telepot
from pprint import pprint
from urllib import parse
import http.client
import urllib.request
import json
import sqlite3
import sys

# API KEY, SERVER
key = '7U2KCB4WfpbyjuvPBbqsz1uOxm4Waddl'
server = 'api.neople.co.kr'
server_id = ['cain', 'diregie', 'siroko', 'prey', 'casillas', 'hilder', 'anton', 'bakal']

# API URL


# TELEGRAM TOKEN, MY CHAT ID
TOKEN = '586425069:AAH1R8tLZ7Ynq8nGVA5zJu-Zq9IJ0b9rbbU'
MY_CHATID = '568233093'

MAX_MSG_LENGTH = 300

bot = telepot.Bot(TOKEN)

def connectOpenAPIServer():
    global conn, server
    conn = http.client.HTTPSConnection(server)
    conn.set_debuglevel(1)

def getCharacterList(character_name):
    global conn, key, server_id

    if conn == None:
        connectOpenAPIServer()

#    res.list = []
    encText = urllib.parse.quote(character_name)

    for serverId in server_id :
        conn.request("GET", "/df/servers/" + serverId + "/characters?characterName=" + encText + "&wordType=full&apikey=" + key)
        req = conn.getresponse()
        print(serverId)

        if int(req.status) == 200:
            response_body = req.read()
            print(response_body, type(response_body))
            print("\n---------------여기까지출력됨---------------\n")
            decode_response_body = response_body.decode('utf-8')
            print(decode_response_body)

            print(type(decode_response_body))

            json_response_body = json.loads(decode_response_body)
            dic_character_data = json_response_body['rows'][0]
            #        print(type(json_response_body))
            print(dic_character_data['characterName'])




def run(data_param) :
    conne = sqlite3.connect('logs.db')
    cursor = conne.cursor()
    cursor.execute('CREAT TABLE IF NOT EXISTS logs(user TEXT, log TEXT, PRIMARY KEY(user, log))')
    conne.commit()

    user_cursor = sqlite3.connect('users.db').cursor()
    user_cursor.execute('CREATE TABLE IF NOT EXISTS users(user TEXT, character_id TEXT, PRIMARY KEY(user, character_id))')
    user_cursor.execute('SELECT * from users')

    #for data in user_cursor.fetchall() :


connectOpenAPIServer()
