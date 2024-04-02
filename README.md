# Проект укорачивания ссылок
## **Основная цель проекта**
Изучение возможностей фреймворка [Flask](https://flask.palletsprojects.com/en/3.0.x/) 
## **Описание проекта**
Данное приложение создает случайную короткую ссылку при незаполненном поле короткой ссылки.
Также можно ввести свой вариант, используя доступный регистр (буквы A-Z и цифры).
## **Стек**
* Python v3+
* Flask
## **Запуск проекта**
Выполните следующие команды в терминале:
1. Клонировать проект из репозитория
```shell
git clone git@github.com:waynje/yacut.git
```
2. Создать, активировать виртуальное окружение и в него установить зависимости:
```shell
cd yacut
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
3. Запустить проект из командной строки:
```shell
flask run
```
После запуска проект будет доступен по адресу: http://127.0.0.1:5000
## _Работа API_
**Эндпоинты**
```shell
"/api/id/"
"/api/id/{short_id}/"
```
**Запросы**
Получение полного URL по короткой ссылке:
```shell
Method: GET
Endpoint: "/api/id/{short_id}/"
```
Создание короткой ссылки:
```shell
Method: POST
Endpoint: "/api/id/"
Payload:
{
    "url": "string",
    "custom_id": "string",
}
```
* Автор: ([Юрий Агеев](https://github.com/waynje))