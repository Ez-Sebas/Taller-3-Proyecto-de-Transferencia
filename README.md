# Sistema de Gestión de Usuarios

Sistema en Python con menú interactivo en consola que permite gestionar usuarios localmente mediante operaciones CRUD (Crear, Leer, Actualizar, Eliminar), con persistencia en archivos y código organizado por módulos.

## 🗂️ Estructura del proyecto:

```
gestion-usuarios/
├─ README.md                         
├─ requirements.txt
├─ .gitignore
├─ data/
│  └─ records.json                  # o registros.csv / registros.txt
└─ src/
      ├─ main.py                    # punto de entrada
      ├─ menu.py                    # interfaz de consola (UI)
      ├─ service.py                 # lógica (CRUD)
      ├─ file.py                    # persistencia (leer/guardar)
      ├─ validate.py                # validaciones y helpers
      └─ integration.py             # faker / pandas / requests
```

## ▶️ Instalación:

1. Clona el repositorio:
   ```bash
   git clone <url-del-repositorio>
   cd taller3_python
   ```
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecuta el programa:
   ```bash
   python src/main.py
   ```

## 💻 Uso:

Al ejecutar el programa, se mostrará un menú interactivo en consola:

1. Crear usuario
2. Listar usuarios
3. Buscar usuario
4. Actualizar usuario
5. Eliminar usuario
0. Salir

Flujo básico:
   Crear un usuario ingresando:
   - ID
   - Nombre
   - Correo
   - Edad
   - Estado

   Consultar usuarios registrados
   Buscar un usuario por su ID
   Actualizar los datos de un usuario existente
   Eliminar un usuario

El sistema mostrará mensajes claros indicando si la operación fue exitosa o si ocurrió algún error.

## 👤 Créditos/Autores:
Sebastián Zuleta Echavarría — Ficha 3406211

## 📄 Licencia:
Información sobre el uso permitido del código.