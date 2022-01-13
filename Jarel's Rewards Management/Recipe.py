class Recipe:
    recipe_id = 0

    def __init__(self, name, desc, price, ing1, ing2, ing3, ing4, ing5, img):
        Recipe.recipe_id += 1
        self.__recipe_id = Recipe.recipe_id
        self.__name = name
        self.__desc = desc
        self.__price = price
        self.__ing1 = ing1
        self.__ing2 = ing2
        self.__ing3 = ing3
        self.__ing4 = ing4
        self.__ing5 = ing5
        self.__img = img

    def get_recipe_id(self):
        return self.__recipe_id

    def get_name(self):
        return self.__name

    def get_desc(self):
        return self.__desc

    def get_price(self):
        return self.__price

    def get_ing1(self):
        return self.__ing1

    def get_ing2(self):
        return self.__ing2

    def get_ing3(self):
        return self.__ing3

    def get_ing4(self):
        return self.__ing4

    def get_ing5(self):
        return self.__ing5

    def get_img(self):
        return self.__img

    def set_recipe_id(self, recipe_id):
        self.__recipe_id = recipe_id

    def set_name(self, name):
        self.__name = name

    def set_desc(self, desc):
        self.__desc = desc

    def set_price(self, price):
        self.__price = price

    def set_ing1(self, ing1):
        self.__ing1 = ing1

    def set_ing2(self, ing2):
        self.__ing2 = ing2

    def set_ing3(self, ing3):
        self.__ing3 = ing3

    def set_ing4(self, ing4):
        self.__ing4 = ing4

    def set_ing5(self, ing5):
        self.__ing5 = ing5

    def set_img(self, img):
        self.__img = img
