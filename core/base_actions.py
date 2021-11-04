import asyncio
import datetime

from core.base_queue import BaseQueue
from core.session import Session

from database.actions import calculation_actions, category_actions, user_actions

from middleware.check_if_have_rights import check_if_have_rights


class BaseActions(BaseQueue):
    def __init_(self, queue: asyncio.Queue, session: Session):
        super().__init__(queue, session)
        self.session = Session
        self.queue = queue

    async def clear_data(self) -> bool:
        """Чистит только поля юзера, есть глобальный метод очистить все, доступен только админу"""
        if check_if_have_rights(self.session.get_user()):
            calculation_action = calculation_actions.CalculateActions(self.session.get_user())
            calculation_action.clear_data()
            return True
        return False

    async def write_data(self) -> bool:
        """Дает пользователю ввести расход"""
        if check_if_have_rights(self.session.get_user()):
            calculate_action = calculation_actions.CalculateActions(self.session.get_user())
            category_action = category_actions.CategoryActions()
            print(category_action.get_all_categoryes())
            category = input('Введите категорию, все существующие категории вы можете увидеть выше,'
                             'если их нет, то создайте.')
            category = category_action.get_categoryes_by_name(category)
            price = int(input("Введите цену товара"))
            date = input(
                "Введите время на когда добавить расход, или просто нажмите ентер если вам нужно текущее время\n"
                "Пример формата '%Y-%m%-d'")
            if not date:
                date = datetime.datetime.now()
            else:
                date = datetime.datetime.strptime(date, "%Y-%m-%d")
            calculate_action.create_consumption(price=price, date=date, category_id=category)
            return True
        return False

    async def create_category(self) -> bool:
        """Создает категорию"""
        if check_if_have_rights(self.session.get_user()):
            category_action = category_actions.CategoryActions()
            answer = input("Введите название категории")
            category_action.create_category(answer)
            return True
        return False

    # TODO Знаю, так не особо красиво делать, я бы вынес их в инициазилатор, но где-то ошибка начала выскакивать,
    # не best practices уж точно
    async def get_statistic_by_month(self):
        calculation_action = calculation_actions.CalculateActions(self.session.get_user())
        month = input("Введите месяц по которому нужно выбрать")
        stat = calculation_action.get_stat_by_month(month)
        return stat

    async def get_statistic_by_day(self):
        calculation_action = calculation_actions.CalculateActions(self.session.get_user())
        day = int(input("Введите день по которому нужно выбрать"))
        stat = calculation_action.get_stat_by_day(day)
        return stat

    async def get_statistic_by_year(self):
        calculation_action = calculation_actions.CalculateActions(self.session.get_user())
        year = int(input("Введите год по которому нужно выбрать"))
        stat = calculation_action.get_stat_by_year(year)
        return stat


    async def get_all_statistic(self):
        calculation_action = calculation_actions.CalculateActions(self.session.get_user())
        stat = calculation_action.get_stat_by_all_categories()
        return stat

    async def get_statistic_by_category(self):
        calculation_action = calculation_actions.CalculateActions(self.session.get_user())
        category = input("Введите id категории")
        stat = calculation_action.get_stat_by_category(category)
        return stat
