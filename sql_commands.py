import sqlite3 as sql

#conn = sql.connec
def create_database(db_name, table_name):
    # Подключение к базе данных или создание новой, если её нет
    conn = sql.connect(db_name)
    c = conn.cursor()
    
    # Создание таблицы в базе данных
    c.execute(f"CREATE TABLE {table_name}(id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
    
    # Сохранение изменений и закрытие соединения
    conn.commit()
    conn.close()

#create_database("database.db", "table_name")