from database.models import User
from email.utils import parseaddr


class UserActions:

    def create_user(self, name: str, surname: str, email: str, password: str, role="User"):
        if self.valid_user_email(email)[1]:
            try:
                z = User.create(name=name, surname=surname, email=email, password=password, role=role)
            except:
                return False
            return True
        return False

    @staticmethod
    def valid_user_email(email) -> tuple:
        return parseaddr(email)

    @staticmethod
    def get_user(email, password):
        try:
            a = User.select().where(User.email == email, User.password == password).first()
            return a
        except:
            return False

    @staticmethod
    def get_user_by_id(user_id):
        try:
            return User.get_by_id(user_id)
        except:
            return False

    def check_user_role(self, id_of_user):
        try:
            user = self.get_user_by_id(id_of_user)
            return user.role
        except:
            return False
