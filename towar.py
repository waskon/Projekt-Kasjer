from datetime import datetime
import random

item_names = ["Pietruszka", "Arbuz", "Chleb", "Makaron", "Śledź", "Agrest",
              "Banan", "Ziemniak", "Batat", "Pomidor", "Jabłko", "Cytryna",
              "Czekolada", "Pomarańcza", "Gruszka", "Kapusta", "Kiwi", "Groch",
              "Granat", "Tuńczyk"]


class Towar:

    def __init__(self):
        self.append_time = datetime.now()
        self.validate_time = datetime.now()
        self.name = random.choice(item_names)


class TowarNaSztuki(Towar):

    def __init__(self):
        super().__init__()
        self.quantity = self.getQuantity()

    @staticmethod
    def getQuantity():
        is_more_than_one = random.choice([True, False])
        return random.randint(2, 50) if is_more_than_one else 1


class TowarNaWage(Towar):

    def __init__(self):
        super().__init__()
        self.weight = round(random.uniform(0.05, 2), 2)
        self.weighed = False
