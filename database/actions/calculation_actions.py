import datetime

from database.models import Calculation, Category


class CalculateActions():
    def __init__(self, user):
        self.user = user

    def create_consumption(self, price: int, category_id: Category, date: datetime.datetime):
        Calculation.create(user=self.user, price=price, category_id=category_id, date=date)

    def clear_data(self):
        all_data_for_deleting = Calculation.select().where(Calculation.user == self.user)
        for i in all_data_for_deleting:
            Calculation.delete_by_id(i)

    def get_stat_by_day(self, day):
        res = Calculation.select().where(Calculation.date.day == day and Calculation.user == self.user)
        data = []
        for i in res:
            data.append({
                "Цена": i.price,
                "Пользователь": i.user.name,
                "Категория": i.category.name_of_category,
                "Дата добавленияя": i.date
            })
        return data

    def get_stat_by_year(self, year):
        res = Calculation.select().where(Calculation.date.year == year and Calculation.user == self.user)
        data = []
        for i in res:
            data.append({
                "Цена": i.price,
                "Пользователь": i.user.name,
                "Категория": i.category.name_of_category,
                "Дата добавленияя": i.date
            })
        return data

    def get_stat_by_month(self, month):
        res = Calculation.select().where(Calculation.date.month == month and Calculation.user == self.user)
        data = []
        for i in res:
            data.append({
                "Цена": i.price,
                "Пользователь": i.user.name,
                "Категория": i.category.name_of_category,
                "Дата добавленияя": i.date
            })
        return data

    def get_stat_by_all_categories(self):
        res = Calculation.select().where(Calculation.user == self.user)
        data = []
        for i in res:
            data.append({
                "Цена": i.price,
                "Пользователь": i.user.name,
                "Категория": i.category.name_of_category,
                "Дата добавленияя": i.date
            })
        return data

    def get_stat_by_category(self, category_id):
        res = Calculation.select().where(Calculation.category == category_id and Calculation.user == self.user)
        data = []
        print(res)
        for i in res:
            data.append({
                "Цена": i.price,
                "Пользователь": i.user.name,
                "Категория": i.category.name_of_category,
                "Дата добавленияя": i.date
            })
        return data

