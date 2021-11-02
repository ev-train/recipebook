# Recipes API

## Настройки

Положить в файл `recipes_book/settings_local.py`

* DB_HOST - хост PostgreSQL
* DB_NAME - название базы
* DB_USER - пользователь
* DB_PASSWORD - пароль

## Запуск проекта

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 main.py
```