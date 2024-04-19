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

def get_columns(db_name):
    conn = sql.connect(db_name)
    c = conn.cursor()
    c.execute("SELECT * FROM table_name")
    columns = [description[0] for description in c.description]
    conn.commit()
    conn.close()
    return columns


def get_rows(db_name):
    conn = sql.connect(db_name)
    c = conn.cursor()
    c.execute("SELECT * FROM table_name")
    rows = c.fetchall()
    conn.commit()
    conn.close()
    print(rows)
    return rows

#create_database("database.db", "table_name")