import random
import unittest
from database.actions.user_actions import UserActions
from database.models import User
import string
import random

user_actions = UserActions()


class UserTest(unittest.TestCase):

    def test_creating_user(self):
        lst_ = []
        for i in range(10):
            lst_.append(random.choice(string.ascii_letters))
        email = ''.join(lst_)
        print(email)
        self.assertEqual(True, user_actions.create_user("Danil", "Grechkas", f'{email}@gmail.com', "gdasdasd3004"))

    def test_fail_creating_user(self):
        self.assertEqual(False, user_actions.create_user("asdsad", "sdasd", 'asdsad', 'asdsd'))

    def test_get_user_by_id(self):
        self.assertEqual(User.get_by_id(1), user_actions.get_user_by_id(1))

    def test_valid_user_email(self):
        email = user_actions.valid_user_email('grecigor11@gmail.com')[1]
        self.assertEqual('grecigor11@gmail.com', email)
