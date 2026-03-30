def eliminar_persona():
    seleccion = tree.focus()
    if seleccion:
        id_persona = tree.item(seleccion, 'values')[0]
        conn = conectar_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Personas WHERE id=?", (id_persona,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Éxito", "Registro eliminado.")
        limpiar_campos()
        cargar_datos()
