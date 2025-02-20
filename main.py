import os
import schedule
import vk_api
import json
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

import pytz
from datetime import datetime
time_zone = pytz.timezone('Europe/Moscow')

access_token=os.environ.get("VK_BOT_TOKEN")

bot_session = vk_api.VkApi(token=access_token)
bot_api = bot_session.get_api()

def main():
    load_sections_schedules()
    schedule.every().minute.do(sequence)
    while True:
        schedule.run_pending()

def load_sections_schedules():
    global timetable
    with open('timetable.json') as f:
        timetable = json.load(f)
    f.close()

def sequence():
    global current_weekday, current_time
    current_weekday = datetime.now(time_zone).isoweekday()
    current_time = datetime.now(time_zone).time().strftime("%H:%M")
    find_duty_section()
    monday_notification()
    send_to_duty_section()

def find_duty_section():
    global duty_section_id
    duty_section_id = (datetime.now(time_zone).isocalendar().week) % len(timetable['schedules'])

def monday_notification():
    if current_weekday == 1 and current_time == "09:00" : # Monday 9:00
        message = "На этой неделе дежурит " + str(timetable['schedules'][duty_section_id]['section_name'])
        bot_session.method("messages.send", {"peer_id":int(timetable['maint_chat_id']), "message":message,"random_id":0})
        load_sections_schedules()

def send_to_duty_section():
    for schedule in timetable['schedules'][duty_section_id]['schedule']:
        workout_weekday = schedule['weekday']
        if current_weekday == int(workout_weekday):
            workout_start = schedule['start']
            workout_end = schedule['end']
            if current_time == str(workout_start) or current_time == str(workout_end):
                message = "Дружественное напоминание о дежурстве 🙌" #+ str(timetable['schedules'][duty_section_id]['section_name'])
                bot_session.method("messages.send", {"peer_id":timetable['schedules'][duty_section_id]['chat_id'], "message":message,"random_id":0})

if __name__ == '__main__':
    main()
