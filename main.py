import os
import schedule
import vk_api
import json
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

import pytz
from datetime import datetime
time_zone = pytz.timezone('Europe/Moscow')

# Переделать на сбор данных из json
sections = [ "Сценбой", "Истфех", "секция Танцев", "Фаершоу", "Лучная секция" ]
sections_chats = [ 2000000001, 2000000001, 2000000001, 2000000001, 2000000001 ]
main_chat_id = 2000000001

access_token=os.environ.get("VK_BOT_TOKEN")

bot_session = vk_api.VkApi(token=access_token)
bot_api = bot_session.get_api()

def main():
    load_sections_schedules()
    schedule.every().second.do(sequence)
    while True:
        schedule.run_pending()

def sequence():
    find_duty_section()
    monday_notification()
    send_to_duty_section()

def find_duty_section():
    global duty_section_id
    duty_section_id = (datetime.now(time_zone).isocalendar().week) % len(sections)

def monday_notification():
    if datetime.now(time_zone).isoweekday() == 1 and datetime.now(time_zone).time().strftime("%H:%M:%S") == "09:00:00" : # Monday 9:00
        monday_message = "На этой неделе дежурит ", sections[duty_section_id]
        bot_session.method("messages.send", {"peer_id":main_chat_id, "message":monday_message,"random_id":0})
        load_sections_schedules()

def send_to_duty_section():
    print(schedules_json) 
    #print("without tz: ", datetime.now().isoweekday())
    #print("with tz: ", datetime.now(time_zone).isoweekday())
    #print(datetime.now(time_zone).time())
    #print("duty_section_id: ", duty_section_id)

def load_sections_schedules():
    global schedules_json
    with open('data.json') as f:
        schedules_json = json.load(f)
   
if __name__ == '__main__':
    main()
