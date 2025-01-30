import sqlite3

# Підключення до бази (створиться файл database.db у папці PREFECT)
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Створення таблиці, якщо вона ще не існує
cursor.execute('''
    CREATE TABLE IF NOT EXISTS medals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        medal_type TEXT NOT NULL,
        count INTEGER NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

# Збереження змін
conn.commit()
conn.close()

print("✅ Таблиця 'medals' створена успішно!")
