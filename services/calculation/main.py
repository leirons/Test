from core.base_queue import BaseQueue
from core.actions import Actions
from core.session import Session
from database.actions import user_actions
import asyncio


class Client:

    @staticmethod
    async def read(z):
        await z.task_reader()

    @staticmethod
    async def write(z):
        await z.task_writer()

    def log_in(self, user_actions: user_actions.UserActions):
        email = input("Введите емайл")
        password = input("Введите парол")

        user = user_actions.get_user(email, password)
        return user

    def run(self):
        actions = user_actions.UserActions()
        ask = input("Вы зарегестрированы?")
        if ask.lower() != "yes":
            name = input('Введите имя')
            surname = input("Введите фамилию")
            email = input("Введите емайл")
            password = input("Пароль")
            actions.create_user(name=name, surname=surname, email=email, password=password)
            print('Теперь ввойдите')

        user = self.log_in(user_actions=actions)
        session = Session(user)

        queue = asyncio.Queue()
        z = Actions(queue, session)

        loop = asyncio.get_event_loop()

        asyncio.ensure_future(self.read(z))
        asyncio.ensure_future(self.write(z))

        loop.run_forever()


if __name__ == '__main__':
    client = Client()
    client.run()