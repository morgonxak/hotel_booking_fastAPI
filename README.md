

## Заметки
миграции:
* alembic revision --autogenerate -m "inition migration"
* alembic upgrade head
* alembic downgrade -1

* docker run -d -e POSTGRES_PASSWORD=asm123 -p 5432:5432 postgres
* docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=asm123 -d postgres
