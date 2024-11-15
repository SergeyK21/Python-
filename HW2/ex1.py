import logging
from functools import reduce

logger = logging.getLogger('ex1')
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

fh = logging.FileHandler(
    filename='log_file_1.log',
    mode='w',
    encoding='utf-8'
)
fh.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

ch.setFormatter(formatter)
fh.setFormatter(formatter)

logger.addHandler(ch)
logger.addHandler(fh)


class Wallet:
    convert = {'RUB': 1, 'USD': 62.1, 'EUR': 69.7}  # по состоянию на 1 января 2020 г.

    def __init__(self, owner_name, RUB=0.0, USD=0.0, EUR=0.0):
        if isinstance(owner_name, str):
            self.owner_name = owner_name
        else:
            raise ValueError("Имя владельца должно быть строковым типом!")
        self.assets = {}
        self.assets['RUB'] = RUB
        self.assets['USD'] = USD
        self.assets['EUR'] = EUR

    def __iter__(self):
        return iter(self.assets.items())

    def __str__(self):
        return f'{self.owner_name}: ' \
               f'{self.assets["RUB"]:.2f} {"RUB"}, ' \
               f'{self.assets["USD"]:.2f} {"USD"}, ' \
               f'{self.assets["EUR"]:.2f} {"EUR"}'

    def __float__(self):
        return reduce(lambda a, x: a + (self.assets[x] * self.convert[x]), self.assets.keys(), 0)

    def __int__(self):
        return int(reduce(lambda a, x: a + (1 if self.assets[x] else 0), self.assets.keys(), 0))

    def __bool__(self):
        return int(reduce(lambda a, x: a + (1 if self.assets[x] != 0 else 0), self.assets.keys(), 0)) == 3

    def __eq__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return reduce(lambda a, x: a + (self.assets[x] * self.convert[x]), self.assets.keys(), 0) == other
        elif isinstance(other, Wallet):
            return reduce(lambda a, x: a + (self.assets[x] * self.convert[x]), self.assets.keys(), 0) == float(
                other)
        else:
            raise Exception('Ошибка!')

    def __lt__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return reduce(lambda a, x: a + (self.assets[x] * self.convert[x]), self.assets.keys(), 0) < other
        elif isinstance(other, Wallet):
            return reduce(lambda a, x: a + (self.assets[x] * self.convert[x]), self.assets.keys(), 0) < float(
                other)
        else:
            raise Exception('Ошибка!')

    def __gt__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return reduce(lambda a, x: a + (self.assets[x] * self.convert[x]), self.assets.keys(), 0) > other
        elif isinstance(other, Wallet):
            return reduce(lambda a, x: a + (self.assets[x] * self.convert[x]), self.assets.keys(), 0) > float(
                other)
        else:
            raise Exception('Ошибка!')

    def __sub__(self, other):
        if isinstance(other, tuple) and len(other) == 2:
            if other[0] == 'RUB':
                temp = self.assets['RUB'] - other[1]
                if temp < 0:
                    raise Exception("Ошибка!")
                return Wallet(
                    self.owner_name,
                    RUB=temp,
                    USD=self.assets['USD'],
                    EUR=self.assets['EUR']
                )
            elif other[0] == 'USD':
                temp = self.assets['USD'] - other[1]
                if temp < 0:
                    raise Exception("Ошибка!")
                return Wallet(
                    self.owner_name,
                    RUB=self.assets['RUB'],
                    USD=temp,
                    EUR=self.assets['EUR']
                )
            elif other[0] == 'EUR':
                temp = self.assets['EUR'] - other[1]
                if temp < 0:
                    raise Exception("Ошибка!")
                return Wallet(
                    self.owner_name,
                    RUB=self.assets['RUB'],
                    USD=self.assets['USD'],
                    EUR=temp
                )
            else:
                raise Exception('Ошибка!')

        elif isinstance(other, Wallet):
            return Wallet(
                self.owner_name,
                RUB=(self.assets['RUB'] - other['RUB']) if (self.assets['RUB'] - other['RUB']) > 0 else 0,
                USD=(self.assets['USD'] - other['USD']) if (self.assets['USD'] - other['USD']) > 0 else 0,
                EUR=(self.assets['EUR'] - other['EUR']) if (self.assets['EUR'] - other['EUR']) > 0 else 0
            )
        else:
            raise Exception('Ошибка!')

    def __add__(self, other):
        if isinstance(other, tuple) and len(other) == 2:
            if other[0] == 'RUB':
                temp = self.assets['RUB'] + other[1]
                if temp < 0:
                    raise Exception("Ошибка!")
                return Wallet(
                    self.owner_name,
                    RUB=temp,
                    USD=self.assets['USD'],
                    EUR=self.assets['EUR']
                )
            elif other[0] == 'USD':
                temp = self.assets['USD'] + other[1]
                if temp < 0:
                    raise Exception("Ошибка!")
                return Wallet(
                    self.owner_name,
                    RUB=self.assets['RUB'],
                    USD=temp,
                    EUR=self.assets['EUR']
                )
            elif other[0] == 'EUR':
                temp = self.assets['EUR'] + other[1]
                if temp < 0:
                    raise Exception("Ошибка!")
                return Wallet(
                    self.owner_name,
                    RUB=self.assets['RUB'],
                    USD=self.assets['USD'],
                    EUR=temp
                )
            else:
                raise Exception('Ошибка!')

        elif isinstance(other, Wallet):
            return Wallet(
                self.owner_name,
                RUB=self.assets['RUB'] + other['RUB'],
                USD=self.assets['USD'] + other['USD'],
                EUR=self.assets['EUR'] + other['EUR']
            )
        else:
            raise Exception('Ошибка!')

    def __getitem__(self, key):
        if key == 'RUB' or key == 'USD' or key == 'EUR':
            return self.assets[key]
        else:
            raise Exception('Ошибка!')

    def __setitem__(self, key, value):
        if (key == 'RUB' or key == 'USD' or key == 'EUR') and (isinstance(value, float) or isinstance(value, int)):
            self.assets[key] = value
        else:
            raise Exception('Ошибка!')


ivan_wallet = Wallet(owner_name="Иван Иванов")
petr_wallet = Wallet(owner_name="Петр Петров",
                     RUB = 50000,
                     USD = 250,
                     EUR = 900)


alex_wallet = Wallet(owner_name="Алексей Алексеев",
                     RUB = 100000,
                     USD = 0,
                     EUR = 0)

logger.debug("Добавление")
logger.info("Добавление")
print(petr_wallet.assets)

petr_wallet = petr_wallet - ('USD', 50)
print(str(petr_wallet))

logger.debug("Вычитание")
logger.info("Вычитание")
try:
    alex_wallet = alex_wallet - ('USD', 50)
except Exception as ex:
    print(ex)
    logger.debug(ex)

alex_wallet = alex_wallet + ('EUR', 100)
petr_wallet = petr_wallet + alex_wallet
logger.debug("Сложение")
logger.info("Сложение")

print(alex_wallet)
print(petr_wallet)
