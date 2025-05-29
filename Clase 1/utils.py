import getpass
import re
from colorama import Fore, Style

EMAIL_REGEX = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'

def is_valid_email(email: str) -> bool:
    try:
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(pattern, email) is None:
            return False
        # Verificar que no existan puntos consecutivos
        if '..' in email:
            return False
        return True
    except Exception as e:
        print(Fore.RED + f"❌ Error en validación de email: {e}")
        return False

def input_non_empty(prompt, validate_email=False):
    """Solicita al usuario un input no vacío, opcionalmente valida email."""
    while True:
        try:
            value = input(prompt).strip()
            if not value:
                print(Fore.RED + "❌ Este campo no puede estar vacío.")
            elif validate_email and not is_valid_email(value):
                print(Fore.RED + "❌ Email inválido. Intente de nuevo.")
            else:
                return value
        except Exception as e:
            print(Fore.RED + f"❌ Error en la entrada: {e}")

def input_password_non_empty(prompt):
    while True:
        try:
            password = getpass.getpass(Fore.YELLOW + prompt + Style.RESET_ALL)
            if password.strip():
                return password
            else:
                print(Fore.RED + "❌ La contraseña no puede estar vacía." + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"❌ Error al ingresar la contraseña: {e}")

def is_valid_password(password):
    try:
        # Al menos una mayúscula
        if not re.search(r'[A-Z]', password):
            return False
        # Al menos un número
        if not re.search(r'\d', password):
            return False
        return True
    except Exception as e:
        print(Fore.RED + f"❌ Error en validación de contraseña: {e}")
        return False
