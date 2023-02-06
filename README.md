# Пульт охраны банка

Инструмент для просмотра информации об активных пропусках сотрудников и посещения им хранилища.

### Как установить

- Python3 должен быть уже установлен.
- Используйте `pip` для установки необходимых компонентов:

```
pip install -r requirements.txt
```
- Настройки базы данных и сайта необходимо указать в файле `.env`, расположенном рядом с `manage.py`
```angular2html
# database
HOST = 'my_host.org'
PORT = '1234'
NAME = 'db_name'
USER = 'user'
PASSWORD = 'password'

# site
SECRET_KEY = 'REPLACE_ME'
DEBUG = false
```

### Как запустить

Для запуска скрипта в командной строке перейдите в папку в которой лежит файл main.py. Затем запустите
скрипт следующей командой

  ```
  python manage.py runserver
  ``` 

После загрузки тестового вэб-сервера в консоли будет выведено следующее сообщение:

```angular2html
System check identified no issues (0 silenced).
{CURRENT DATE AND TIME}
Django version 3.2, using settings 'project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

Откройте в браузере ссылку [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
