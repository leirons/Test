from database.models import User, Category


class CategoryActions:
    def __init__(self):
        pass

    def create_category(self, name_of_category: str):
        if name_of_category:
            Category.create(name_of_category=name_of_category)
            return True
        return False

    @staticmethod
    def get_categories_by_name(name_of_category):
        return Category.select().where(Category.name_of_category == name_of_category).first()

    @staticmethod
    def get_all_categoryes():
        categories = [category.name_of_category for category in Category.select()]
        return categories
