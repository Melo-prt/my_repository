class Building:

    total = 0
    def __init__(self, name):
        self.name = name

    def func(self):
        while self.total < 40:
            self.total += 1
            print(self.total)

dom = Building('Дом')

dom.func()



