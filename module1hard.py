grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print(students)
print(type(students))
students2 = list(students)
print(type(students2))
students2.sort()    # нашла такую сортировку, ибо до другой не смогла додуматься
print(students2)

print(type(grades))
print(len(grades))
a = len(grades[0])
b = len(grades[1])
c = len(grades[2])
d = len(grades[3])
e = len(grades[4])
print(a, b, c, d, e)

a = sum(grades[0])/a
b = sum(grades[1])/b
c = sum(grades[2])/c
d = sum(grades[3])/d
e = sum(grades[4])/e
print(a, b, c, d, e)

print({students2[0]: a, students2[1]: b, students2[2]: c, students2[3]: d, students2[4]: e})





