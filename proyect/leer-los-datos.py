def cargar_datos():
    for item in tree.get_children():
        tree.delete(item)
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Personas")
    for fila in cursor.fetchall():
        tree.insert("", "end", values=fila)
    conn.close()