import sqlite3

db = sqlite3.connect('player.db')
cursor = db.cursor()
sql = 'SELECT * FROM player;'
cursor.execute(sql)
results = cursor.fetchall()
print(results)

db.close()