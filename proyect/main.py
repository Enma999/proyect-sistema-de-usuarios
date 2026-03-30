import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# ---------------------------------------------------------
# RAMA 1: feature/db-connection
# ---------------------------------------------------------
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

# ---------------------------------------------------------
# RAMA 2: feature/read-personas
# ---------------------------------------------------------
def cargar_datos():
    for item in tree.get_children():
        tree.delete(item)
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Personas")
    for fila in cursor.fetchall():
        tree.insert("", "end", values=fila)
    conn.close()

# ---------------------------------------------------------
# RAMA 3: feature/create-personas
# ---------------------------------------------------------
def guardar_persona():
    nombre, edad, rol = entry_nombre.get(), entry_edad.get(), entry_rol.get()
    if nombre and edad and rol:
        conn = conectar_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Personas (nombre, edad, rol) VALUES (?, ?, ?)", (nombre, edad, rol))
        conn.commit()
        conn.close()
        messagebox.showinfo("Éxito", "Persona registrada correctamente.")
        limpiar_campos()
        cargar_datos()
    else:
        messagebox.showwarning("Error", "Todos los campos son obligatorios.")

# ---------------------------------------------------------
# RAMA 4: feature/update-personas
# ---------------------------------------------------------
def actualizar_persona():
    seleccion = tree.focus()
    if seleccion:
        id_persona = tree.item(seleccion, 'values')[0]
        nombre, edad, rol = entry_nombre.get(), entry_edad.get(), entry_rol.get()
        if nombre and edad and rol:
            conn = conectar_db()
            cursor = conn.cursor()
            cursor.execute("UPDATE Personas SET nombre=?, edad=?, rol=? WHERE id=?", (nombre, edad, rol, id_persona))
            conn.commit()
            conn.close()
            messagebox.showinfo("Éxito", "Datos actualizados correctamente.")
            limpiar_campos()
            cargar_datos()
        else:
            messagebox.showwarning("Error", "Todos los campos son obligatorios.")

# ---------------------------------------------------------
# RAMA 5: hotfix/ui-delete-fix
# ---------------------------------------------------------
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

# --- Funciones auxiliares ---
def limpiar_campos():
    entry_nombre.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_rol.delete(0, tk.END)

def seleccionar_fila(event):
    seleccion = tree.focus()
    if seleccion:
        valores = tree.item(seleccion, 'values')
        limpiar_campos()
        entry_nombre.insert(0, valores[1])
        entry_edad.insert(0, valores[2])
        entry_rol.insert(0, valores[3])

# ---------------------------------------------------------
# INTERFAZ GRÁFICA DECORADA (Añadir a main o dev inicialmente)
# ---------------------------------------------------------
root = tk.Tk()
root.title("Sistema de Usuarios")
root.geometry("550x500")
root.configure(bg="#2C3E50") # Fondo azul oscuro elegante

# Estilos personalizados
style = ttk.Style()
style.theme_use("clam")
style.configure("TFrame", background="#2C3E50")
style.configure("TLabel", background="#2C3E50", foreground="#ECF0F1", font=("Segoe UI", 10, "bold"))
style.configure("TButton", font=("Segoe UI", 10, "bold"), background="#2980B9", foreground="white", padding=6)
style.map("TButton", background=[("active", "#3498DB")])
style.configure("Treeview", font=("Segoe UI", 10), rowheight=25, background="#ECF0F1")
style.configure("Treeview.Heading", font=("Segoe UI", 11, "bold"), background="#34495E", foreground="white")

# Título Principal
tk.Label(root, text="👨‍💻 Sistema de Usuarios", font=("Segoe UI", 18, "bold"), bg="#2C3E50", fg="#F1C40F", pady=15).pack(fill="x")

# Frame para los inputs
frame_inputs = ttk.Frame(root)
frame_inputs.pack(pady=10)

ttk.Label(frame_inputs, text="Nombre:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_nombre = tk.Entry(frame_inputs, font=("Segoe UI", 10), width=30)
entry_nombre.grid(row=0, column=1, padx=10, pady=5)

ttk.Label(frame_inputs, text="Edad:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_edad = tk.Entry(frame_inputs, font=("Segoe UI", 10), width=30)
entry_edad.grid(row=1, column=1, padx=10, pady=5)

ttk.Label(frame_inputs, text="Rol:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_rol = tk.Entry(frame_inputs, font=("Segoe UI", 10), width=30)
entry_rol.grid(row=2, column=1, padx=10, pady=5)

# Frame para los botones
frame_botones = ttk.Frame(root)
frame_botones.pack(pady=10)

ttk.Button(frame_botones, text="💾 Guardar", command=guardar_persona).grid(row=0, column=0, padx=10)
ttk.Button(frame_botones, text="✏️ Actualizar", command=actualizar_persona).grid(row=0, column=1, padx=10)
ttk.Button(frame_botones, text="🗑️ Eliminar", command=eliminar_persona).grid(row=0, column=2, padx=10)

# Frame para la tabla
frame_tabla = ttk.Frame(root)
frame_tabla.pack(fill="both", expand=True, padx=20, pady=10)

columnas = ("ID", "Nombre", "Edad", "Rol")
tree = ttk.Treeview(frame_tabla, columns=columnas, show="headings")
for col in columnas:
    tree.heading(col, text=col)
    tree.column(col, width=100, anchor="center")

tree.pack(fill="both", expand=True)
tree.bind("<ButtonRelease-1>", seleccionar_fila)

# Iniciar la aplicación
conectar_db()
cargar_datos()
root.mainloop()