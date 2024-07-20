def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    try:
        for i in numbers:
            try:
                result += i
            except TypeError:
                incorrect_data += 1
    except TypeError:
        incorrect_data += 1
    return result, incorrect_data


def calculate_average(numbers):
    result_1 = personal_sum(numbers)
    try:
        result = result_1[0] / (len(numbers) - result_1[1])
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан неверный тип данных')
        return None
    else:
        return result

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать

