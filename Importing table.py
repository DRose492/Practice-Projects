import sqlite3

def execute_sql_script(db_file, sql_script_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    with open(sql_script_file, 'r') as sql_file:
        sql_script = sql_file.read()

    cursor.executescript(sql_script)

    conn.commit()
    conn.close()

db_file_path = 'D:\demon\Documents\Python Code\SDEV_220_Final_Project_Group7\data.db'

sql_script_file_path = r'D:\demon\Documents\Python Code\SDEV_220_Final_Project_Group7\addData.sql'

execute_sql_script(db_file_path, sql_script_file_path)