import queue
from threading import Thread
from random import randint
from time import sleep


class Table:

    def __init__(self, number: int):
        self.number = number
        self.guest = None


class Guest(Thread):

    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))

    def __str__(self):
        return self.name


class Cafe:
    queue = queue.Queue()
    guest_in_table = []

    def __init__(self, *tables: Table):
        self.tables = tables

    def guest_arrival(self, *guests: Guest):
        for i in range(len(guests)):
            for table in self.tables:
                if table.guest is None:
                    table.guest = guests[i]
                    print(f'{table.guest.name} сел(-а) за стол номер {table.number}')
                    guests[i].start()
                    self.guest_in_table.append(guests[i])
                    i += 1
                else:
                    i += 1
                    pass
            if i < len(guests):
                self.queue.put(guests[i])
                print(f'{guests[i].name} в очереди')

    def discuss_guests(self):
        for i in self.guest_in_table:
            for table in self.tables:
                if table.guest == i and i.is_alive:
                    i.join()
                    print(f'{i.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                    if not self.queue.empty():
                        i = self.queue.get()
                        table.guest = i
                        print(f'{i.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                        i.start()
                        self.guest_in_table.append(i)


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
