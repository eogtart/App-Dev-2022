import Reward


class Voucher(Reward.Reward):
    def __init__(self, name, desc, points, date):
        super().__init__(name, desc, points, date, 'Voucher')

    def __str__(self):
        return '{},{},{},{},{}'.format(self.get_name(),
                                       self.get_desc(),
                                       self.get_points(),
                                       self.get_date(),
                                       self.get_type())
