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
    return rows

def get_column_types(db_name):
    conn = sql.connect(db_name)
    c = conn.cursor()
    c.execute("PRAGMA table_info(table_name)")
    column_types = [i[2] for i in c.fetchall()]
    conn.commit()
    conn.close()
    return _sqlite_to_python_type(column_types)

def _sqlite_to_python_type(sqlite_type: list):
    sqlite_to_python = {
        'INTEGER': int,
        'REAL': float,
        'TEXT': str,
        'BLOB': bytes,
        'NULL': type(None)
    }
    return [sqlite_to_python.get(x, str) for x in sqlite_type]

def add_row(db_name, values):
    conn = sql.connect(db_name)
    c = conn.cursor()
    c.execute(f"INSERT INTO table_name VALUES {str(values)}")
    conn.commit()
    conn.close()

def del_row(db_name, values, columns):
    conn = sql.connect(db_name)
    c = conn.cursor()
    c.execute(f"DELETE FROM table_name WHERE {columns[0]} = {values[0]}")
    conn.commit()
    conn.close()



#add_row("db/database.db")


#create_database("database.db", "table_name")