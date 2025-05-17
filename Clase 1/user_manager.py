import hashlib
from colorama import Fore, Style, init

init(autoreset=True)


def hash_password_sha256(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def register_user(users, name, email, password):
    try:
        for user in users:
            if user['email'] == email:
                print(Fore.RED + "❌ Ya existe un usuario con ese email.")
                return users
 
        hashed_password = hash_password_sha256(password)

        users.append({'name': name, 'email': email, 'password': hashed_password})
        print(Fore.GREEN + "✅ Usuario registrado con éxito.")
        return users
    except Exception as e:
        print(Fore.RED + f"❌ Error al registrar usuario: {e}")
        return users

def list_users(users):
    try:
        if not users:
            print(Fore.YELLOW + "📭 No hay usuarios registrados.")
            return
        for idx, user in enumerate(users, 1):
            print(Fore.CYAN + f"{idx}. {user['name']} - {user['email']}")
    except Exception as e:
        print(Fore.RED + f"❌ Error al listar usuarios: {e}")

def search_users(users, name):
    try:
        results = [user for user in users if name.lower() == user['name'].lower()]
        if results:
            for user in results:
                print(Fore.MAGENTA + f"🔍 {user['name']} - {user['email']}")
        else:
            print(Fore.RED + "❌ No se encontraron usuarios con ese nombre.")
    except Exception as e:
        print(Fore.RED + f"❌ Error al buscar usuario: {e}")

def delete_user(users, email):
    try:
        new_users = [user for user in users if user['email'] != email]
        if len(new_users) == len(users):
            print(Fore.RED + "❌ Usuario no encontrado.")
        else:
            print(Fore.GREEN + "🗑️ Usuario eliminado.")
        return new_users
    except Exception as e:
        print(Fore.RED + f"❌ Error al eliminar usuario: {e}")
        return users
