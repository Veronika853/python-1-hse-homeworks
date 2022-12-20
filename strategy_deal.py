class StrategyDeal:
    def __init__(self, bank, start_price, stop_price, targets, source_currency, target_currency):
        self.bank = bank
        self.start_price = start_price
        self.stop_price = stop_price
        self.targets = targets
        self.source_currency = source_currency
        self.target_currency = target_currency

    def __str__(self):
        string_targets = ''
        round_num = 3
        target_percents = self.get_target_percents()
        target_banks = self.get_target_banks()
        target_currency_count = round(self.get_target_currency_count(), round_num)
        target_sizes = self.get_target_sizes()
        total_loss = round(self.get_loss(), round_num)
        total_target_income = round(sum(target_sizes), round_num)
        total_percent = round(self.get_total_percent(), round_num)
        transaction_delimiter = '----------------------------------------------'

        for i in range(len(self.targets)):
            string_targets += \
                f'''{i + 1} target: {round(self.targets[i], round_num)} {self.source_currency}
Percent: {round(target_percents[i], round_num)}%
Bank: {round(target_banks[i], round_num)} {self.source_currency}
Target size: {round((target_currency_count / len(self.targets)), round_num)} * {self.targets[i]:} \
= {round(target_sizes[i], round_num)} {self.source_currency}

'''
        output = \
            f'''BANK: {self.bank}
START_PRICE: {self.start_price}
STOP_PRICE: {round(self.stop_price, round_num)}; {round(self.bank, round_num)} - {round(self.stop_price, round_num)} \
* {target_currency_count} = {total_loss} {self.source_currency}
PAIR: {self.target_currency}-{self.source_currency}

''' + string_targets + \
            f'''Strategy income: {total_target_income} - {self.bank} = {round(total_target_income - self.bank, 3)} \
{self.source_currency}; percent: {total_percent}%

{transaction_delimiter}
'''
        return output

    def get_target_percents(self):
        start_price = self.start_price
        return list(map(lambda target: round((target - start_price) / start_price * 100, 10), self.targets))

    def get_targets(self):
        return self.targets

    def get_target_banks(self):
        bank = self.bank
        target_percents = self.get_target_percents()
        return list(map(lambda x: (1 + x / 100) * bank, target_percents))

    def get_target_currency_count(self):
        return self.bank / self.start_price

    def get_loss(self):
        target_currency_count = self.get_target_currency_count()
        return self.bank - self.stop_price * target_currency_count

    def get_target_sizes(self):
        target_currency_count = self.get_target_currency_count()
        targets_count = len(self.targets)
        targets = self.get_targets()
        return list(map(lambda target: target_currency_count / targets_count * target, targets))

    def get_total_income(self):
        target_sizes = self.get_target_sizes()
        return sum(target_sizes)

    def get_total_percent(self):
        return round((self.get_total_income() - self.bank) / self.bank * 100, 10)

    def print_transaction(self):
        return self.__str__()
