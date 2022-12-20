from task_io import read, write
from strategy_deal import StrategyDeal

TRANSACTION_DELIMETER = '-----'


def get_transactions(data):
    transactions = []
    for i in data.split(TRANSACTION_DELIMETER + '\n'):
        transactions.append(list(filter(lambda x: x != '' and '---' not in x and x != 'Покупка', i.split('\n'))))
    return transactions


def parse_transaction(transaction):
    bank = 0
    start_price = 0
    stop_price = 0
    targets = []
    currencies = []

    for i in transaction:
        if 'BANK:' in i:
            bank = float(i.lstrip('BANK: '))
        if 'Вход:' in i:
            start_price = float(i.lstrip('Вход: '))
        if 'Выход:' in i:
            stop_price = float(i.lstrip('Выход: '))
        if 'Таргет:' in i:
            targets = i.lstrip('Таргет: ').split(';')
            targets = list(map(float, targets))
        if '-' in i:
            currencies = i.split('-')

    return StrategyDeal(bank, start_price, stop_price, targets, currencies[1], currencies[0])


def main():
    output = ''
    data = read()
    transactions = get_transactions(data)
    objects = []
    for i in transactions:
        objects.append(parse_transaction(i))

    for i in objects:
        output += i.print_transaction()

    write(output)
    print('Done, result in out.txt')


if __name__ == "__main__":
    main()
