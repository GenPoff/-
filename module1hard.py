# Список оценок
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# Множество имен учеников
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# Список имен учеников в алфавитном порядке
students = sorted(students)

# Словарь для хранения среднего балла каждого ученика
average_grades = {}

# Перебираем имена учеников
for student in students:  # Отсортированный список имен учеников
    total_score = sum(grades[students.index(student)])  # Сумма оценок текущего ученика
    count = len(grades[students.index(student)])        # Количество оценок текущего ученика
    average_grade = total_score / count                 # Средний балл текущего ученика

    average_grades[student] = average_grade

print(average_grades)