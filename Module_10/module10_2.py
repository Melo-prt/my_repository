from threading import Thread
import time


class Knight(Thread):
    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        enemy = 100
        day = 0
        while enemy > 0:
            enemy -= self.power
            day += 1
            time.sleep(1)
            print(f'{self.name} сражается {day} дней, осталось {enemy} воинов.\n')
        print(f'{self.name} одержал победу за {day} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')
