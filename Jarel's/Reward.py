class Reward:
    reward_id = 0

    def __init__(self, name, desc, points, date, type):
        Reward.reward_id += 1
        self.__reward_id = Reward.reward_id
        self.__name = name
        self.__desc = desc
        self.__points = points
        self.__date = date
        self.__type = type

    def get_reward_id(self):
        return self.__reward_id

    def get_name(self):
        return self.__name

    def get_desc(self):
        return self.__desc

    def get_points(self):
        return self.__points

    def get_date(self):
        return self.__date

    def get_type(self):
        if self.__type == 'U':
            return "Unknown"
        else:
            return self.__type

    def set_reward_id(self, reward_id):
        self.__reward_id = reward_id

    def set_name(self, name):
        self.__name = name

    def set_desc(self, desc):
        self.__desc = desc

    def set_points(self, points):
        self.__points = points

    def set_date(self, date):
        self.__date = date

    def set_type(self, type):
        self.__type = type




