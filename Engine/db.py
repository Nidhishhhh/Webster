from http.client import CREATED
import sqlite3

from flask.cli import run_command

conn = sqlite3.connect("webster.db")
cursor = conn.cursor()

#query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR (1000))"
#cursor.execute(query)


#Notion
#query = "INSERT INTO sys_command VALUES (null, 'notion', 'C:\\Users\\Nidhu\\AppData\\Local\\Programs\\Notion\\Notion.exe')"
#cursor.execute(query)
#conn.commit()

#Discord
#query = "INSERT INTO sys_command VALUES (null, 'Discord', 'C:\\Users\\Nidhu\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Discord Inc\\Discord.lnk')"
#cursor.execute(query)
#conn.commit()

#query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR (1000))"
#cursor.execute(query)


#Instagram
#query = "INSERT INTO web_command VALUES (null, 'instagram', 'https://www.instagram.com/')"
#cursor.execute(query)
#conn.commit()

#YouTube
#query = "INSERT INTO web_command VALUES (null, 'youtube', 'https://www.youtube.com/')"
#cursor.execute(query)
#conn.commit()


#query = """
#CREATE TABLE IF NOT EXISTS info (
#    name VARCHAR(100),
#    designation VARCHAR(50),
#    mobileno VARCHAR(40),
#    email VARCHAR(200),
#    city VARCHAR(300)
#)
#"""

#cursor.execute(query)
#conn.commit()

#print("Table created successfully")

#conn.close()


# Create a table with the desired columns
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS contacts (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name VARCHAR(200),
#     mobile_no VARCHAR(255),
#     email VARCHAR(255),
#     address VARCHAR(255)
# )
# """)

# conn.commit()

# print("Contacts table created successfully")

# # Verify table exists
# cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
# print(cursor.fetchall())

# conn.close()

cursor.execute("PRAGMA table_info(sys_command)")
print(cursor.fetchall())

