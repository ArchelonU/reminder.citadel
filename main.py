import os
import schedule
import vk_api
import json
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

import pytz
from datetime import datetime, timedelta
time_zone = pytz.timezone('Europe/Moscow')

access_token=os.environ.get("VK_BOT_TOKEN")

bot_session = vk_api.VkApi(token=access_token)
bot_api = bot_session.get_api()

def main():
    load_timetables()
    sequence() # Требуется для первого запуска без ожидания истечения времени выставленного в модуле schedule.
    schedule.every().minute.do(sequence)
    while True:
        schedule.run_pending()

def load_timetables():
    global timetables
    with open('timetables.json') as f:
        timetables = json.load(f)
    f.close()

def sequence():
    global current_date, current_weekday, current_time, duty_id

    current_date = datetime.now(time_zone)
    current_weekday = current_date.isoweekday()
    current_time = current_date.time().strftime("%H:%M")
    duty_id = (current_date.isocalendar().week) % len(timetables['schedules'])

    monday_notifications()
    duty_notification()
    load_timetables()

def monday_notifications():
    if current_weekday == 1 :
        match current_time:
            case "09:00" : # Monday 9:00
                message = "На этой неделе дежурит " + str(timetables['schedules'][duty_id]['section_name'])
                bot_session.method("messages.send", {"peer_id":int(timetables['main_chat_id']), "message":message,"random_id":0})
            case "14:00" : # Monday 14:00
                previus_date =  current_date - timedelta(days=7)
                if current_date.month != previus_date.month :
                    for section in timetables['schedules']:
                        message = "Напоминаю о сдаче взносов 💲💲💲 Казна сама себя не наполнит!"
                        bot_session.method("messages.send", {"peer_id":section['chat_id'], "message":message,"random_id":0})

def duty_notification():
    for workout_schedule in timetables['schedules'][duty_id]['workout_schedule']:
        workout_weekday = workout_schedule['weekday']
        if current_weekday == int(workout_weekday):
            workout_start = workout_schedule['start']
            workout_end = workout_schedule['end']
            if current_time == str(workout_start) or current_time == str(workout_end):
                message = "Дружественное напоминание о дежурстве 🙌"
                bot_session.method("messages.send", {"peer_id":timetables['schedules'][duty_id]['chat_id'], "message":message,"random_id":0})

if __name__ == '__main__':
    main()
