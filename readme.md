## Запуск программы в виртуальном окружении

Установить необходимые программные пакеты:  
`sudo apt install pip python3-venv`

Создать директорию виртуального окружения:  
`sudo python3 -m venv /opt/reminder.citadel/`

Переопределить pip для работы в текущем виртуальном окружении:  
`sudo /opt/reminder.citadel/bin/pip install --upgrade pip`

Установить в виртуальном окружении необходимые пакеты:  
`sudo /opt/reminder.citadel/bin/pip install schedule vk_api`

Запуск программы из виртуального окружения:  
`/opt/reminder.citadel/bin/python3 ./reminder.citadel.py`
