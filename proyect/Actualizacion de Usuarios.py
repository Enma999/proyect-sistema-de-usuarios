def seleccionar_fila(event):
    seleccion = tree.focus()
    if seleccion:
        valores = tree.item(seleccion, 'values')
        limpiar_campos()
        entry_nombre.insert(0, valores[1])
        entry_edad.insert(0, valores[2])
        entry_rol.insert(0, valores[3])

def actualizar_persona():
    seleccion = tree.focus()
    if seleccion:
        id_persona = tree.item(seleccion, 'values')[0]
        nombre, edad, rol = entry_nombre.get(), entry_edad.get(), entry_rol.get()
        conn = conectar_db()
        cursor = conn.cursor()
        cursor.execute("UPDATE Personas SET nombre=?, edad=?, rol=? WHERE id=?", (nombre, edad, rol, id_persona))
        conn.commit()
        conn.close()
        cargar_datos()