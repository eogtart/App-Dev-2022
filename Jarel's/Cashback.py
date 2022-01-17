import Reward


class Cashback(Reward.Reward):
    def __init__(self, name, desc, points, date):
        super().__init__(name, desc, points, date, 'Cashback')

    def __str__(self):
        return '{},{},{},{},{}'.format(self.get_name(),
                                       self.get_desc(),
                                       self.get_points(),
                                       self.get_date(),
                                       self.get_type())
