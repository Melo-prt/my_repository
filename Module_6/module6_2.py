class Venicle:
    __COLOR_VARIANTS = ['red', 'black', 'blue']
    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = str(owner)
        self.__model = str(__model)
        self.__engine_power = int(__engine_power)
        self.__color = str(__color)

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
       print(self.get_model())
       print(self.get_horsepower())
       print(self.get_color())
       print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        self.new_color = str(new_color)
        if self.new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = self.new_color
        else:
            print(f'Нельзя сменить цвет на {self.new_color}')

class Sedan(Venicle):
    __PASSENGERS_LIMIT = 5

volvo = Sedan('Ivan', 't1000', '3', 'Black')

volvo.print_info()
volvo.set_color('Red')
volvo.set_color('White')
volvo.print_info()

