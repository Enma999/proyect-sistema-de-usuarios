def conectar_db():
    conn = sqlite3.connect('sistema_personas.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Personas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            edad INTEGER NOT NULL,
            rol TEXT NOT NULL
        )
    ''')
    conn.commit()
    return conn