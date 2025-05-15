# file_handler.py
import json
from decouple import config
from colorama import Fore, init

init(autoreset=True)

def load_users():
    try:
        with open(config('USER_FILE'), 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(Fore.YELLOW + "⚠️ Archivo de usuarios no encontrado. Se creará uno nuevo al guardar.")
        return []
    except json.JSONDecodeError:
        print(Fore.RED + "⚠️ Error al cargar usuarios, archivo corrupto.")
        return []

def save_users(users):
    try:
        with open(config('USER_FILE'), 'w') as f:
            json.dump(users, f, indent=2)
        print(Fore.GREEN + "💾 Usuarios guardados correctamente.")
    except Exception as e:
        print(Fore.RED + f"❌ Error al guardar usuarios: {e}")
