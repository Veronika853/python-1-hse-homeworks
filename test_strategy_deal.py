from unittest import TestCase
from strategy_deal import StrategyDeal

class TestStrategyDeal(TestCase):
    def test_get_target_percents(self):
        object = StrategyDeal(5000, 20, 16.2, [24.4, 25.5, 26.4345], 'EGT', 'YDQ')
        target_percents = object.get_target_percents()
        self.assertEqual([22.0, 27.5, 32.1725], target_percents)

    def test_get_targets(self):
        object = StrategyDeal(5000, 20, 16.2, [24.4, 25.5, 26.4345], 'EGT', 'YDQ')
        targets = object.get_targets()
        self.assertEqual([24.4, 25.5, 26.4345], targets)

    def test_get_target_banks(self):
        object = StrategyDeal(5000, 20, 16.2, [24.4, 25.5, 26.4345], 'EGT', 'YDQ')
        target_banks = object.get_target_banks()
        self.assertEqual([6100.0, 6375.0, 6608.625], target_banks)

    def test_get_target_currency_count(self):
        object = StrategyDeal(5000, 20, 16.2, [24.4, 25.5, 26.4345], 'EGT', 'YDQ')

    def test_get_loss(self):
        object = StrategyDeal(5000, 20, 16.2, [24.4, 25.5, 26.4345], 'EGT', 'YDQ')
        loss = object.get_loss()
        self.assertEqual(950.0, loss)

    def test_get_target_sizes(self):
        object = StrategyDeal(5000, 20, 16.2, [24.4, 25.5, 26.4345], 'EGT', 'YDQ')
        target_sizes = object.get_target_sizes()
        self.assertEqual([2033.333333333333, 2125.0, 2202.875], target_sizes)

    def test_get_total_income(self):
        object = StrategyDeal(5000, 20, 16.2, [24.4, 25.5, 26.4345], 'EGT', 'YDQ')
        total_income = object.get_total_income()
        self.assertEqual(6361.208333333333, total_income)

    def test_get_total_percent(self):
        object = StrategyDeal(5000, 20, 16.2, [24.4, 25.5, 26.4345], 'EGT', 'YDQ')
        total_percent = object.get_total_percent()
        self.assertEqual(27.2241666667, total_percent)

