grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
a = sorted(students)
dict_ = {}
dict_.update({a[0]:grades[0], a[1]:grades[1], a[2]:grades[2], a[3]:grades[3], a[4]:grades[4]})
dict_[a[0]] = sum(grades[0]) / len(grades[0])
dict_[a[1]] = sum(grades[1]) / len(grades[1])
dict_[a[2]] = sum(grades[2]) / len(grades[2])
dict_[a[3]] = sum(grades[3]) / len(grades[3])
dict_[a[4]] = sum(grades[4]) / len(grades[4])
print(dict_)