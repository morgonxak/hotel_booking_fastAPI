# hotel_booking_fastAPI

Тестовый проект на фреймворке FastAPI.


## dev
### postgres
```bash
------------- Запускаем базу данных postgres -------------
docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=asm123 -d postgres

------------- Повторный запуск образа -------------------
docker run -d -e POSTGRES_PASSWORD=asm123 -p 5432:5432 postgres
```
### Меграция
```bash
------------- Создать файл меграции -------------
alembic revision --autogenerate -m "inition migration"

------------- Провести миграцию -------------
alembic upgrade head

------------- Откатить миграцию -------------
alembic downgrade -1
```

