import os
import schedule
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

from datetime import datetime

sections = [ "Сценбой", "Истфех", "Танцы", "Фаершоу", "Лучная секция" ]
sections_chats = [ 2000000001, 2000000001, 2000000001, 2000000001, 2000000001 ]

access_token=os.environ.get("VK_BOT_TOKEN")

bot_session = vk_api.VkApi(token=access_token)
bot_api = bot_session.get_api()
#peer_id = 2000000001 # <--- СЮДА_ВСТАВИТЬ_ID_БЕСЕДЫ

#peer_id = bot_api.messages.searchConversations(q='Тест Ботов', count=1)['items'][0]['peer']['local_id']

def find_duty_section():
    duty_number = (datetime.now().isocalendar().week) % len(sections)
    send_duty_section(duty_number)

def send_duty_section(duty_number):
    #text_message = "Напоминаю, что сегодня дежурит секция "+sections[duty_number]
    #bot_session.method("messages.send", {"peer_id":sections_chats[duty_number], "message":text_message,"random_id":0})
    
    peer_id = bot_api.messages.searchConversations(q='peer=Тест Ботов', count=1)#['items'][0]['peer']['local_id']
    print(peer_id)

def main():
    #schedule.every().monday.at('09:00').do(find_duty_section)
    schedule.every().second.do(find_duty_section)
    while True:
        schedule.run_pending()

if __name__ == '__main__':
    main()
