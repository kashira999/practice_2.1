import math

with open('resource/numbers.txt', 'w') as f:
    for i in range(1, 1001):
        f.write(str(i) + '\n')

print("Файл numbers.txt создан с числами от 1 до 1000")
print("=" * 60)

const = 73 ** 2 + 29
print(f"Константа (73² + 29) = {const}")
print("=" * 60)

input_file = open('resource/numbers.txt', 'r')
output_file = open('resource/result.txt', 'w')

output_file.write("Числа кратные 7 и результат вычислений:\n")
output_file.write("=" * 50 + "\n")

count = 0
for line in input_file:
    num = int(line.strip())

    if num % 7 == 0:
        result = num * 100 / const
        output_file.write(f"{num} -> {result:.2f}\n")
        print(f"Найдено: {num} -> {result:.2f}")
        count += 1

input_file.close()
output_file.close()

print("=" * 60)
print(f"Готово! Найдено {count} чисел, кратных 7")
print("Результат сохранен в result.txt")