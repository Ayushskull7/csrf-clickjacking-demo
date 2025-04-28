import sqlite3

conn = sqlite3.connect('demo.db')
c = conn.cursor()
# Create a users table with username and password
c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
''')
# Insert a demo user (username: demo@gmail.com, password: demo123)
c.execute("INSERT OR IGNORE INTO users (username, password) VALUES ('demo@gmail.com', 'demo123')")
conn.commit()
conn.close()

print("Database initialized with sample user demo@gmail.com")
