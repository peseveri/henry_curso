# 📘 Sistema de Gestión de Usuarios (Consola)

Este proyecto simula un sistema básico de gestión de usuarios en Python, interactuando por consola y guardando los datos en un archivo `.json`.

## ✅ Funcionalidades

- Registrar usuarios (nombre, email, contraseña)
- Validación de contraseña: debe contener al menos una letra mayúscula y un número
- Uso de manejo de errores con try/except
- Listar usuarios
- Buscar usuarios por nombre (búsqueda exacta)
- Eliminar usuarios
- Guardar y cargar usuarios desde archivo `.json`
- Validación de emails con expresiones regulares
- Entrada de contraseña con visualización oculta, mostrando solo la primera letra (usando `getpass` personalizado)
- Mensajes en consola con colores usando `colorama`
- Pruebas unitarias con `unittest`

## 🧪 Tecnologías usadas

- Python 3.10+
- Colorama — para colorear la interfaz de consola
- python-decouple — para cargar variables desde `.env`
- Regex — para validar emails
- unittest — para tests básicos

## ⚙️ Requisitos

- Python 3.10 o superior
- Entorno virtual recomendado para aislar dependencias

## Nota Importante sobre el archivo .env
  El archivo .env NO se subira al repositorio ni compartido públicamente, ya que suele contener variables de configuración sensibles.
  En este proyecto, se usa la variable:
  USER_FILE=users.json

  Para que el programa funcione correctamente, cada usuario debe crear su propio archivo .env localmente con esta variable.

  ## Cómo crear el archivo .env
    En la raíz del proyecto, crea un archivo llamado .env
    Agrega esta linea:
      USER_FILE=users.json
    Guarda el archivo y no lo subas a Git ni a ningún repositorio público.

## 🚀 Instalación

Clonar el repositorio:

git clone <URL-del-repo>  
cd <nombre-del-repo>

Crear y activar entorno virtual:

python -m venv venv  

En Windows:  
.\venv\Scripts\activate  

En Linux/macOS:  
source venv/bin/activate  

Instalar dependencias:

pip install -r requirements.txt

Crear archivo `.env` en la raíz con:  

USER_FILE=users.json

## ▶️ Ejecución

Ejecutar la aplicación:

python main.py

Seguir las instrucciones en consola para gestionar usuarios.

## 🧪 Tests

Para correr los tests unitarios:

python -m unittest discover

## 📄 Licencia

MIT License

## 👤 Autor

Pedro Severi
