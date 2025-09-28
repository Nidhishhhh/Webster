import sqlite3

conn = sqlite3.connect("webster.db")
cursor = conn.cursor()

query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR (1000))"
cursor.execute(query)


#Notion
query = "INSERT INTO sys_command VALUES (null, 'notion', 'C:\\Users\\Nidhu\\AppData\\Local\\Programs\\Notion\\Notion.exe')"
cursor.execute(query)
conn.commit()

#Discord
#query = "INSERT INTO sys_command VALUES (null, 'Discord', 'C:\\Users\\Nidhu\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Discord Inc\\Discord.lnk')"
#cursor.execute(query)
#conn.commit()

query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR (1000))"
cursor.execute(query)


#Instagram
query = "INSERT INTO web_command VALUES (null, 'instagram', 'https://www.instagram.com/')"
cursor.execute(query)
conn.commit()

#YouTube
query = "INSERT INTO web_command VALUES (null, 'youtube', 'https://www.youtube.com/')"
cursor.execute(query)
conn.commit()


