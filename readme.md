### Подготовка к работе
Для запуска программы необходимо установить дополнительные библиотеки **python** (рекомендуется делать это в виртуальном окружении) и прописать токен бота в переменные окружения.  
Для этого, сначала необходимо установить программные пакеты **pip** и **python3-venv**:  
`sudo apt update && sudo apt -y install pip python3-venv`

Затем создать директорию виртуального окружения, например **/opt/reminder.citadel/**:  
`sudo python3 -m venv /opt/reminder.citadel/`

После чего можно проверить обновления для **pip** в виртуальном окружении:  
`sudo /opt/reminder.citadel/bin/pip install --upgrade pip`

И уже в виртуальном окружении установить используемые пакеты **pytz**, **schedule** и **vk_api**:  
`sudo /opt/reminder.citadel/bin/pip install pytz schedule vk_api`

Запуск программы необходимо осуществлять интерпретатором из виртуального окружения с указанием расположения основного файла программы:  
`/opt/reminder.citadel/bin/python3 /home/user/reminder.citadel/main.py`

---
Для отправки сообщений, необходимо прописать токен бота в переменные окружения.
Сделать это можно прописав строку в файл **/etc/bash.bashrc**, или в файл **.bashrc** из домашней директории пользователя, из под которого будет выполняться программа в будущем:
`echo "export VK_BOT_TOKEN=\"token_example_1234567890\"" >> /etc/bash.bashrc`

Для использования указанной переменной в рамках текущей сессии, необходимо проинициализировать изменения в файле (либо перезайти):
`source /etc/bash.bashrc`

---
Для упращения запуска, можно сделать алиас, вызывающий нужный интерпретатор с аргументом, содержащим полный путь до основного файла программы:  
`alias reminder.citadel.py="/opt/reminder.citadel/bin/python3 /home/user/reminder.citadel/main.py"`

Чтобы алиас работал для всех пользователей, данную строку можно поместить в **/etc/bash.bashrc** (для чего снова потребуются права суперпользователя), например, так:
`echo "alias reminder.citadel.py=\"/opt/reminder.citadel/bin/python3 /home/user/reminder.citadel/main.py\"" >> /etc/bash.bashrc`

После добавления строки, необходимо либо перезайти, либо перечитать файл **/etc/bash.bashrc**:  
`source /etc/bash.bashrc`

----
### Автоматизация запуска
Автоматизацию запуска можно сделать через создание `systemd` сервиса, либо с помощью `supervisor`, который помимо запуска может ещё и отслеживать состояние работы.

Для использования `supervisor`, необходимо установить его пакет в созданное виртуальное окружение:
`sudo /opt/reminder.citadel/bin/pip install supervisor`

И при запуске, указать необходимый конфигурационный файл:
`sudo /opt/reminder.citadel/bin/supervisord -c /home/user/reminder.citadel/supervisord.conf`