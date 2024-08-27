grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades = [[sum(grades[0])/len(grades[0])], [sum(grades[1])/len(grades[1])], [sum(grades[2])/len(grades[2])], [sum(grades[3])/len(grades[3])], [sum(grades[4])/len(grades[4])]]
print(sorted(students))
students = {'Aaron': grades[0], 'Bilbo': grades[1], 'Johnny': grades[2], 'Khendrik': grades[3], 'Steve': grades[4]}
print(students)
while 1:print(students.get(input('Введите имя ученика: '),'Такого ученика нет '))


