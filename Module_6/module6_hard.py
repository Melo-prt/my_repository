import math


class Figure:
    sides_count = 0

    def __init__(self, color, sides, filled=False):
        if self.__is_valid_sides(*sides):
            if isinstance(self, Cube):
                self.__sides = list(sides) * 12
            else:
                self.__sides = list(sides)
        else:
            self.__sides = [1] * self.sides_count
        self.__color = list(color)
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(value, int) and 0 <= value <= 255 for value in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        else:
            print('Заданы неверные параметры цвета.')

    def __is_valid_sides(self, *sides):
        if isinstance(self, Cube):
            cond_1 = len(sides) == 1
        else:
            cond_1 = len(sides) == self.sides_count
        cond_2 = all([isinstance(side, int) and side > 0 for side in sides])
        return cond_1 and cond_2

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            if isinstance(self, Cube):
                self.__sides = list(new_sides) * 12
            else:
                self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, sides)
        self.__radius = self.__len__() / (2 * math.pi)
        self.square = math.pi * (self.__radius ** 2)

    def get_radius(self):
        return self.__radius

    def get_square(self):
        return self.square


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, sides)
        self.__square = math.sqrt(
            (self.__len__() / 2) * (self.__len__() - self.get_sides()[0]) * (self.__len__() - self.get_sides()[1])
            * (self.__len__() - self.get_sides()[2]))
        self.__height = self.get_square() * 2 / self.get_sides()[0]

    def get_square(self):
        return self.__square


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, sides)

    def get_volume(self):
        side = int(self.get_sides()[0])
        return side ** 3


# круг
circle1 = Circle((200, 200, 100), 10)
print('Стороны:', circle1.get_sides())
print('Площадь:', circle1.get_square())
print('Радиус:', circle1.get_radius())
print('Цвета:', circle1.get_color())
circle1.set_color(1, 2, 3)
print('Цвета:', circle1.get_color())
circle1.set_color(-1, 200, 3)
print('Цвета:', circle1.get_color())
circle1.set_color(1, 2, 300.0)
print('Цвета:', circle1.get_color())
circle1.set_sides(10)
print('Стороны:', circle1.get_sides())
print('Площадь:', circle1.get_square()) # не меняет площадь
print('Радиус:', circle1.get_radius()) # не меняет радиус
circle1.set_sides(10, 8)
print('Стороны:', circle1.get_sides())

print('\n\n\n\n\n')

# треугольник
fig = Triangle((200, 200, 100), 10)
print('Стороны:', fig.get_sides())
print('Площадь:', fig.get_square()) # + получение высоты треугольника
print('Цвета:', fig.get_color())

fig = Triangle((200, 200, 100), 10, 7, 9)
print('Стороны:', fig.get_sides())
fig.set_sides(1)
print('Стороны:', fig.get_sides())
fig.set_sides(1, 2, 3)
print('Стороны:', fig.get_sides())
fig.set_sides(1, 2, -3)
print('Стороны:', fig.get_sides())

print('\n\n\n\n\n')
# куб
fig = Cube((200, 200, 100), 10, 12)
print('Стороны:', fig.get_sides())
print('Объем:', fig.get_volume())
print('Цвета:', fig.get_color())

fig = Cube((200, 200, 100), 10)
print('Стороны:', fig.get_sides())
print('Объем:', fig.get_volume())
fig.set_sides(50)
print('Стороны:', fig.get_sides())
fig.set_sides(-100)
print('Стороны:', fig.get_sides())
fig.set_sides(1, 2, 3)
print('Стороны:', fig.get_sides())
fig.set_sides(1, 2, -3)
print('Стороны:', fig.get_sides())
print('Объем:', fig.get_volume())
