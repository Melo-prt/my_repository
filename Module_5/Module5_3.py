class Building:

    def __init__(self, building_type, number_of_floors):
        self.numberOfFloors = number_of_floors
        self.buildingType = building_type

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType

first = Building('Коттедж', 3)
second = Building('Коттедж', 3)
third = Building('Коттедж', 5)

print(first == second)
print(first == third)