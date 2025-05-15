import unittest
from utils import is_valid_email, is_valid_password
from colorama import Fore, Style, init

init(autoreset=True)  # Para que el color se reinicie tras cada print

class TestEmailValidation(unittest.TestCase):
    def test_valid_email(self):
        valid_emails = [
            "user@example.com",
            "user.name@domain.co",
            "user_name@domain.com",
            "user-name@domain.co.uk"
        ]
        for email in valid_emails:
            with self.subTest(email=email):
                try:
                    self.assertTrue(is_valid_email(email), f"El email '{email}' debería ser válido")
                    print(Fore.GREEN + f"✔ test_valid_email pasó para: {email}")
                except Exception as e:
                    print(Fore.RED + f"✘ test_valid_email falló con email '{email}': {e}")
                    self.fail(f"test_valid_email falló con email '{email}': {e}")

    def test_invalid_email(self):
        invalid_emails = [
            "plainaddress",
            "@missingusername.com",
            "username@.com",
            "username@site.",
            "username@site,com",
            "username@site..com",
            "username@site com",
            "username@site#com",
            ""
        ]
        for email in invalid_emails:
            with self.subTest(email=email):
                try:
                    self.assertFalse(is_valid_email(email), f"El email '{email}' debería ser inválido")
                    print(Fore.GREEN + f"✔ test_invalid_email pasó para: {email}")
                except Exception as e:
                    print(Fore.RED + f"✘ test_invalid_email falló con email '{email}': {e}")
                    self.fail(f"test_invalid_email falló con email '{email}': {e}")

class TestPasswordValidation(unittest.TestCase):
    def test_valid_password(self):
        valid_passwords = [
            "Password1",
            "abcD1234",
            "Qwerty9",
            "HelloWorld2023"
        ]
        for pwd in valid_passwords:
            with self.subTest(password=pwd):
                try:
                    self.assertTrue(is_valid_password(pwd), f"La contraseña '{pwd}' debería ser válida")
                    print(Fore.GREEN + f"✔ test_valid_password pasó para: {pwd}")
                except Exception as e:
                    print(Fore.RED + f"✘ test_valid_password falló con contraseña '{pwd}': {e}")
                    self.fail(f"test_valid_password falló con contraseña '{pwd}': {e}")

    def test_invalid_password(self):
        invalid_passwords = [
            "password",       # sin mayúsculas ni números
            "PASSWORD",       # sin números
            "12345678",       # sin mayúsculas
            "pass1234",       # sin mayúsculas
            "PASSword",       # sin números
            "",               # vacía
            "abcde"           # sin mayúscula ni número
        ]
        for pwd in invalid_passwords:
            with self.subTest(password=pwd):
                try:
                    self.assertFalse(is_valid_password(pwd), f"La contraseña '{pwd}' debería ser inválida")
                    print(Fore.GREEN + f"✔ test_invalid_password pasó para: {pwd}")
                except Exception as e:
                    print(Fore.RED + f"✘ test_invalid_password falló con contraseña '{pwd}': {e}")
                    self.fail(f"test_invalid_password falló con contraseña '{pwd}': {e}")

if __name__ == '__main__':
    unittest.main()
