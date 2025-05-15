from user_manager import register_user, list_users, search_users, delete_user
from file_handler import load_users, save_users
from utils import input_non_empty, is_valid_email, input_password_non_empty, is_valid_password
from colorama import Fore, Style, init

init(autoreset=True)

def main():
    try:
        users = load_users()
    except Exception as e:
        print(Fore.RED + f"⚠️ Error cargando usuarios: {e}")
        users = []

    while True:
        try:
            print(Fore.BLUE + "\n📋 Menú de gestión de usuarios")
            print(Fore.CYAN + "1. Registrar usuario")
            print(Fore.CYAN + "2. Listar usuarios")
            print(Fore.CYAN + "3. Buscar usuario")
            print(Fore.CYAN + "4. Eliminar usuario")
            print(Fore.CYAN + "5. Salir")

            option = input(Fore.YELLOW + "Elija una opción: ").strip()

            if option == '1':
                name = input_non_empty(Fore.YELLOW + "Nombre: ")
                while True:
                    email = input_non_empty(Fore.YELLOW + "Email: " + Style.RESET_ALL)
                    if is_valid_email(email):
                        break
                    else:
                        print(Fore.RED + "❌ Email inválido. Por favor, ingrese un email válido." + Style.RESET_ALL)
                while True:
                    password = input_password_non_empty(Fore.YELLOW + "Contraseña: " + Style.RESET_ALL)
                    if is_valid_password(password):
                        break
                    else:
                        print(Fore.RED + "❌ La contraseña debe tener al menos una mayúscula y un número." + Style.RESET_ALL)
                users = register_user(users, name, email, password)
                save_users(users)
            elif option == '2':
                list_users(users)
            elif option == '3':
                name = input_non_empty(Fore.YELLOW + "Buscar nombre: ")
                search_users(users, name)
            elif option == '4':
                while True:
                    email = input_non_empty(Fore.YELLOW + "Email: " + Style.RESET_ALL)
                    if is_valid_email(email):
                        break
                    else:
                        print(Fore.RED + "❌ Email inválido. Por favor, ingrese un email válido." + Style.RESET_ALL)
                users = delete_user(users, email)
                save_users(users)
            elif option == '5':
                print(Fore.GREEN + "👋 ¡Hasta luego!")
                break
            else:
                print(Fore.RED + "❌ Opción inválida. Intente de nuevo.")
        except Exception as e:
            print(Fore.RED + f"⚠️ Ocurrió un error: {e}")

if __name__ == "__main__":
    main()
