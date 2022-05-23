## Apache log parser
Создать сущности
1. "Работник", с полями:<br>
○ имя – char 255<br>
○ номер телефона – char 255<br>
2. "Торговая точка"
○ название<br>
○ ForeignKey к "Работник" (обязательно к заполнению)<br>
3. "Посещение"<br>
○ дата/время<br>
○ ForeignKey к "Торговая точка"<br>
○ latitude – float<br>
○ longitude – float<br>

Сделать методы<br>
Для упрощения задания, вместо полноценной авторизации передавать в каждый
запрос номер телефона Работника.
1. получить список Торговых точек привязанных к переданному номеру телефона<br>
○ в ответе список Торговых точек:<br>
■ PK<br>
○ Название<br>
2. выполнить посещение в Торговую точку<br>
○ принимает:<br>
■ PK Торговой точки<br>
■ координаты<br>
○ в ответе:<br>
■ PK Посещения<br>
■ Дата/время<br>
○ проверять, что переданный номер телефона Работника привязан к
указанной ТТ, в противном случае возвращать ошибку<br>
○ при создании Посещения в дата/время сохранить текущие дату/время
---
# Запуск
0. 
1. запуск
```sh
$ docker-compose -f docker-compose.dev.yml up --build
```

2. закидываем дефолтные данные, включая админа 
```sh
$ docker exec -it app poetry run python manage.py loaddata default_data.json
```
3. админка логин - admin, пароль - 25658545
`http://127.0.0.1:8000/api/swagger/` - документация API

`http://127.0.0.1:8000/admin/` - админка


# TODO
1. Убрать .env.dev из индекса (оставлен для тестового проекта)
2. добавить валидаторы на поля моделей (ограничения долготы ,ширины) - по условия не требуется )))

# Database dump/load
```shell
$ docker exec -it shop_app sh -c "poetry run python manage.py dumpdata --natural-foreign --natural-primary --exclude=contenttypes --exclude=auth.Permission --exclude=admin.logentry --exclude=sessions.session --indent 4 > default_data.json"
$ docker exec -it shop_app poetry run python manage.py loaddata default_data.json
```
## Enter to container
```sh
$ docker exec -it <id container or name> bash
$ docker exec -it <id container or name> poetry run <command>
```
