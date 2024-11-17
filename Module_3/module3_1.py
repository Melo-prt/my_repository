calls = 0


def count_calls():
    global calls
    calls += 1
    return calls


def string_info(string: str):
    res = (len(string), string.upper(), string.lower())
    count_calls()
    return res


def is_contains(string: str, list_to_search: list):
    string = string.lower()
    list_to_search = str(list_to_search).lower()
    count_calls()
    return string in list_to_search


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)