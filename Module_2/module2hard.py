import random
result = ['Пароль: ']
first_stone = random.randint(3, 20)
print('Значение в первом поле:', first_stone)
#a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
a = list(range(21))[1:]
b = list(range(21))[1:]
for i in range(20):
    for j in range(20):
        if i >= j:
            continue
        if first_stone % (a[i] + b[j]) == 0:
            result.append(str(a[i]) + str(b[j]))
print(*result, sep='')