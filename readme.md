### Подготовка к работе
Для начала необходимо определиться с размещением кода. Его можно разместить в домашнюю папку пользователя из под которого он будет запускаться, либо в какую-то общую папку, например **/opt/reminder.citadel**.  
`cd /opt && sudo git clone https://github.com/ArchelonU/reminder.citadel.git`  

При размещении кода в папке с чересчур высокими правами, git'у это не понравится, поэтому для дальнейшей работы с ним потребуется выполнить команду, которая добавит папку в доверенные:  
`git config --global --add safe.directory /opt/reminder.citadel`

Для запуска программы необходимо установить дополнительные библиотеки **python** (рекомендуется делать это в виртуальном окружении) и прописать токен бота в переменные окружения.  
Для этого, сначала необходимо установить программные пакеты **pip** и **python3-venv**:  
`sudo apt update && sudo apt -y install pip python3-venv`

Затем создать директорию виртуального окружения, например **/opt/reminder.citadel/python3-venv/**:  
`sudo python3 -m venv /opt/reminder.citadel/python3-venv/`

После чего можно проверить обновления для **pip** в виртуальном окружении:  
`sudo /opt/reminder.citadel/python3-venv/bin/pip install --upgrade pip`

И уже в виртуальном окружении установить используемые пакеты **pytz**, **schedule** и **vk_api**:  
`sudo /opt/reminder.citadel/python3-venv/bin/pip install pytz schedule vk_api`

Запуск программы необходимо осуществлять интерпретатором из виртуального окружения с указанием расположения основного файла программы:  
`/opt/reminder.citadel/python3-venv/bin/python3 /opt/reminder.citadel/main.py`

---
Для отправки сообщений, необходимо прописать токен бота в переменные окружения.
Сделать это можно прописав строку в файл **/etc/bash.bashrc**, или в файл **.bashrc** из домашней директории пользователя, из под которого будет выполняться программа в будущем:
`echo "export VK_BOT_TOKEN=\"token_example_1234567890\"" >> /etc/bash.bashrc`

Для использования указанной переменной в рамках текущей сессии, необходимо проинициализировать изменения в файле (либо перезайти):
`source /etc/bash.bashrc`

---
Для упращения запуска, можно сделать алиас, вызывающий нужный интерпретатор с аргументом, содержащим полный путь до основного файла программы:  
`alias reminder.citadel.py="/opt/reminder.citadel/python3-venv/bin/python3 /opt/reminder.citadel/main.py"`

Чтобы алиас работал для всех пользователей, данную строку можно поместить в **/etc/bash.bashrc** (для чего снова потребуются права суперпользователя), например, так:
`echo "alias reminder.citadel.py=\"/opt/reminder.citadel/python3-venv/bin/python3 /opt/reminder.citadel/main.py\"" >> /etc/bash.bashrc`

После добавления строки, необходимо либо перезайти, либо перечитать файл **/etc/bash.bashrc**:  
`source /etc/bash.bashrc`

----
### Автоматизация запуска
Автоматизацию запуска можно сделать через создание `systemd` сервиса, либо с помощью `supervisor`, который помимо запуска может ещё и отслеживать состояние работы.

Для использования `supervisor` необходимо установить соответствующий пакет:
`sudo apt update && sudo apt -y install supervisor`

Затем перенести файл конфигурации супервизора для приложения:
`sudo cp /opt/reminder.citadel/supervisor.conf /etc/supervisor/conf.d/reminder.citadel.conf`

После этого можно перезагрузить супервизор для подхвата конфигурации:
`sudo supervisorctl reload`