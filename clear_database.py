import sqlite3

def clear_database():
    # Підключення до бази даних
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Видалення всіх записів
    cursor.execute("DELETE FROM medals")

    # Збереження змін
    conn.commit()
    conn.close()

    print("База даних очищена!")

if __name__ == "__main__":
    clear_database()
