def custom_write(file_name, strings):
    open_file = open(file_name, 'a', encoding='utf-8')
    number_of_string = 0
    strings_positions = {}
    for i in strings:
        number_of_string += 1
        key = (number_of_string, open_file.tell())
        open_file.write(f'{i}\n')
        strings_positions[key] = i
    open_file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)


