file = open('resource/students.txt', 'r', encoding='utf-8')
lines = file.readlines()
file.close()

students = []
names = []
averages = []

for line in lines:
    parts = line.strip().split(':')
    name = parts[0]
    grades_str = parts[1]

    grades = grades_str.split(',')
    for i in range(len(grades)):
        grades[i] = int(grades[i])

    average = sum(grades) / len(grades)

    students.append([name, average])
    names.append(name)
    averages.append(average)

result_file = open('resource/result.txt', 'w', encoding='utf-8')

for student in students:
    if student[1] > 4.0:
        result_file.write(student[0] + ": " + str(student[1]) + "\n")

result_file.close()

max_average = max(averages)
min_average = min(averages)

for student in students:
    if student[1] == max_average:
        best_student = student[0]
    if student[1] == min_average:
        worst_student = student[0]

print("Студент с наивысшим средним баллом:", best_student, "(", max_average, ")")
print("Студент с низким средним баллом:", worst_student, "(", min_average, ")")
print("\nРезультат записан в файл result.txt")