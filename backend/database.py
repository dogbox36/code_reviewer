import sqlite3

def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS code_reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            model_name TEXT,
            code TEXT,
            analysis TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_analysis(model_name, code, analysis):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO code_reviews (model_name, code, analysis) VALUES (?, ?, ?)",
                   (model_name, code, analysis))
    conn.commit()
    conn.close()
