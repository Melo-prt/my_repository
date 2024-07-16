from pprint import pprint
class Product:

    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return str(f'{self.name}, {self.weight}, {self.category}')



class Shop():

    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        products = open(self.__file_name, 'r')
        file = products.read()
        products.close()
        return file

    def add(self, *products: str):
        self.get_products()
        for prod in products:
            #open_read = open(self.__file_name, 'r')
            if prod.name in file:
                print(f'Продукт {prod} уже есть в магазине')
                #open_read.close()
            else:
                #open_read.close()
                open_app = open(self.__file_name, 'a')
                open_app.write(f'{prod}\n')
                open_app.close()




s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)
print(p1.name)
s1.add(p1, p2, p3)

print(s1.get_products())