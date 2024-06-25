class Building:

    total = 0
    def __init__(self, name):
        self.name = name

dom = Building('Дом')

while dom.total < 40:
    dom.total += 1
    print(dom.total)







