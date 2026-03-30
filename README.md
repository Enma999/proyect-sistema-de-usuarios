# CRUD de Usuarios - Programación III

## 📌 Descripción
Este proyecto implementa un sistema CRUD (Crear, Leer, Actualizar y Eliminar) de registro de personas en Python con interfaz gráfica. Se desarrolló aplicando la metodología Git Flow adaptada a los requerimientos de la asignación para el control de versiones.

## ⚙️ Tecnologías
- Python 3
- Tkinter (UI)
- SQLite (Base de datos local)
- Git & GitHub

## 🚀 Funcionalidades
- Crear registros de personas
- Listar datos en una tabla interactiva
- Actualizar registros existentes
- Eliminar personas del sistema

## 🌿 Git Flow aplicado
Se utilizaron las siguientes ramas principales:
- main
- dev
- qa

Adicionalmente, cada funcionalidad fue desarrollada en ramas independientes (ej. `feature/db-connection`, `feature/read-personas`, `feature/create-personas`, `feature/update/personas`, `hotfix/ui-delete-fix`). 

## 🔁 Pull Requests
Se realizaron un total mínimo de 15 Pull Requests en estado Closed/Merged. 

Para cumplir estrictamente con los mandatos de integración, cada rama de trabajo generó 3 Pull Requests directos:
- feature/* → dev
- feature/* → qa
- feature/* → main

## ▶️ Ejecución
```bash
python app.py
