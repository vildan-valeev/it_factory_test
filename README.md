## Apache log parser
Создать сущности
1. "Работник", с полями:
○ имя – char 255
○ номер телефона – char 255
2. "Торговая точка"
○ название
○ ForeignKey к "Работник" (обязательно к заполнению)
3. "Посещение"
○ дата/время
○ ForeignKey к "Торговая точка"
○ latitude – float
○ longitude – float
Сделать методы
Для упрощения задания, вместо полноценной авторизации передавать в каждый
запрос номер телефона Работника.
1. получить список Торговых точек привязанных к переданному номеру телефона
○ в ответе список Торговых точек:
■ PK
○ Название
2. выполнить посещение в Торговую точку
○ принимает:
■ PK Торговой точки
■ координаты
○ в ответе:
■ PK Посещения
■ Дата/время
○ проверять, что переданный номер телефона Работника привязан к
указанной ТТ, в противном случае возвращать ошибку
○ при создании Посещения в дата/время сохранить текущие дату/время

# Запуск
0. добавить LOG_PATH в .env.dev
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

# Database dump/load
```shell
$ docker exec -it app sh -c "poetry run python manage.py dumpdata --natural-foreign --natural-primary --exclude=contenttypes --exclude=auth.Permission --exclude=admin.logentry --exclude=sessions.session --indent 4 > default_data.json"
docker exec -it app poetry run python manage.py loaddata default_data.json
```
## Enter to container
```sh
$ docker exec -it <id container or name> bash
$ docker exec -it <id container or name> poetry run <command>
```
