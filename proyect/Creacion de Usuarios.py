def limpiar_campos():
    entry_nombre.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_rol.delete(0, tk.END)

def guardar_persona():
    nombre, edad, rol = entry_nombre.get(), entry_edad.get(), entry_rol.get()
    if nombre and edad and rol:
        conn = conectar_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Personas (nombre, edad, rol) VALUES (?, ?, ?)", (nombre, edad, rol))
        conn.commit()
        conn.close()
        messagebox.showinfo("Éxito", "Persona registrada")
        limpiar_campos()
        cargar_datos()