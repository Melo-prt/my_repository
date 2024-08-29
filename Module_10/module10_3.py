from random import randint
from threading import Thread, Lock
from time import sleep


class Bank:
    balance = 0
    lock = Lock()

    def deposit(self):
        for i in range(100):
            n = randint(50, 500)
            self.balance += n
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение: {n}. Баланс: {self.balance}.')
            sleep(0.001)

    def take(self):
        for i in range(100):
            x = randint(50, 500)
            print(f'Запрос на {x}')
            if x <= self.balance:
                self.balance -= x
                print(f'Снятие: {x}. Баланс: {self.balance}.')
            else:
                print('Запрос отклонён. Недостаточно средств.')
                self.lock.acquire()


bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')


