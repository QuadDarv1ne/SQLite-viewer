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

def get_tables(db_name):
    con = sql.connect(db_name)
    cursor = con.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    return cursor.fetchall()[0][0]

def get_columns(db_name):
    conn = sql.connect(db_name)
    c = conn.cursor()
    c.execute(f"SELECT * FROM {get_tables(db_name)}")
    columns = [description[0] for description in c.description]
    conn.commit()
    conn.close()
    return columns
#print(get_columns("C:\\Users\\vlama\\Desktop\\data.db"))


def get_rows(db_name):
    conn = sql.connect(db_name)
    c = conn.cursor()
    c.execute(f"SELECT * FROM {get_tables(db_name)}")
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows

def get_column_types(db_name):
    conn = sql.connect(db_name)
    c = conn.cursor()
    c.execute(f"PRAGMA table_info({get_tables(db_name)})")
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
    c.execute(f"INSERT INTO {get_tables(db_name)} VALUES {str(values)}")
    conn.commit()
    conn.close()

def del_row(db_name, values, columns):
    conn = sql.connect(db_name)
    c = conn.cursor()
    conditions = " AND ".join([f"{col} = ?" for col in columns])
    #print(conditions)
    sq = f"DELETE FROM {get_tables(db_name)} WHERE {conditions}"
    c.execute(sq, values)
    conn.commit()
    conn.close()

#del_row("db/database.db", (1,1,1), get_columns("db/database.db"))


#add_row("db/database.db")


#create_database("database.db", "table_name")