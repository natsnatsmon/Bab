import telepot
import noti
from pprint import pprint
import time

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type != 'text' :
        bot.sendMessage(chat_id, '난 텍스트 이외의 메시지는 처리하지 못해요.')
        return

    text = msg['text']
    args = text.split(' ')

    if text.startswith('검색') and len(args) > 1:
        bot.sendMessage(chat_id, '검색 완료')
        replySearchCharacter(args)

    else:
        bot.sendMessage(chat_id, '모르는 명령어입니다!')

def replySearchCharacter(character_name):
    print(character_name)
#    res_list = noti.getCharacterList(character_name)
    msg = ''


bot = telepot.Bot(noti.TOKEN)
pprint(bot.getMe())

bot.message_loop(handle)
print('Listening...')

while 1:
    time.sleep(10)