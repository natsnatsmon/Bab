import telepot
#import noti
import pprint
import time

bot = telepot.Bot('586425069:AAH1R8tLZ7Ynq8nGVA5zJu-Zq9IJ0b9rbbU')

print(bot.getMe())
bot.sendMessage('568233093', 'Hi HY, I\'m DnF In bot!')

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type != 'text' :
        bot.sendMessage(chat_id, '난 텍스트 이외의 메시지는 처리하지 못해요.')
        return

    text = msg['text']
    args = text.split(' ')

    if text.startswith('검색'):
        bot.sendMessage(chat_id, '서버와 캐릭터 이름을 입력해주세요.')




def replySearchCharacter(character_name):
    print(character_name)



#bot = telepot.Bot(bot.TOKEN)
pprint(bot.getMe())

bot.message_loop(handle)
print('Listening...')

while 1:
    time.sleep(10)