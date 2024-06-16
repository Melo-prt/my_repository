def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(3)
print_params(4, 'Книга')
print_params([1,2], 3, 5)
print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = [3, 'string', True]
values_dict = {'a': 7, 'b': False, 'c': 'Hello'}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [9, True]
print_params(*values_list_2, 42)