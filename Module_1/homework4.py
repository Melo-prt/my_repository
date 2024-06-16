immutable_var = 1, True, "String", [1, "apple"]
print(immutable_var)
# immutable_var[0] = 4 # Нельзя изменить элемент кортежа, только элемент списка в нем
immutable_var[3][0] = 3
print(immutable_var)
mutable_list = [1, 2, 3, 'String']
mutable_list[1] = True
print(mutable_list)