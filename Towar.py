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


class TowarNaWage(Towar):

    def __init__(self):
        super().__init__()
        self.weight = round(random.uniform(0.05, 2), 2)
        self.weighed = False

