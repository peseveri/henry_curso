import unittest
from user_manager import register_user, search_users, delete_user

class TestUserManager(unittest.TestCase):

    def setUp(self):
        self.users = [
            {'name': 'Pedro', 'email': 'pedro@example.com', 'password': 'Password1'},
            {'name': 'Ana', 'email': 'ana@example.com', 'password': 'Ana12345'}
        ]

    def test_register_user_new(self):
        try:
            new_users = register_user(self.users.copy(), 'Luis', 'luis@example.com', 'Pass123')
            self.assertEqual(len(new_users), 3)
            self.assertTrue(any(u['email'] == 'luis@example.com' for u in new_users))
        except Exception as e:
            self.fail(f"test_register_user_new falló con excepción: {e}")

    def test_register_user_duplicate_email(self):
        try:
            new_users = register_user(self.users.copy(), 'Pedro', 'pedro@example.com', 'NewPass1')
            self.assertEqual(len(new_users), 2)  # No agrega usuario duplicado
        except Exception as e:
            self.fail(f"test_register_user_duplicate_email falló con excepción: {e}")

    def test_search_users_found(self):
        try:
            results = [user for user in self.users if 'Pedro'.lower() == user['name'].lower()]
            self.assertEqual(len(results), 1)
            self.assertEqual(results[0]['email'], 'pedro@example.com')
        except Exception as e:
            self.fail(f"test_search_users_found falló con excepción: {e}")

    def test_search_users_not_found(self):
        try:
            results = [user for user in self.users if 'Nonexistent'.lower() == user['name'].lower()]
            self.assertEqual(len(results), 0)
        except Exception as e:
            self.fail(f"test_search_users_not_found falló con excepción: {e}")

    def test_delete_user_found(self):
        try:
            new_users = delete_user(self.users.copy(), 'ana@example.com')
            self.assertEqual(len(new_users), 1)
            self.assertFalse(any(u['email'] == 'ana@example.com' for u in new_users))
        except Exception as e:
            self.fail(f"test_delete_user_found falló con excepción: {e}")

    def test_delete_user_not_found(self):
        try:
            new_users = delete_user(self.users.copy(), 'noexiste@example.com')
            self.assertEqual(len(new_users), 2)  # Sin cambios
        except Exception as e:
            self.fail(f"test_delete_user_not_found falló con excepción: {e}")

if __name__ == '__main__':
    unittest.main()
