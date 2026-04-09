file = open('resource/text.txt', 'w', encoding='utf-8')
file.write("Привет мир\n")
file.write("Как дела?\n")
file.write("Я учу Python\n")
file.write("Сегодня хороший день\n")
file.write("Пока пока\n")
file.close()

file = open('resource/text.txt', 'r', encoding='utf-8')
lines = file.readlines()
file.close()

for i in range(len(lines)):
    lines[i] = lines[i].strip()

print("Количество строк:", len(lines))

words_count = 0
for line in lines:
    words = line.split()
    words_count = words_count + len(words)
print("Количество слов:", words_count)

longest = lines[0]
for line in lines:
    if len(line) > len(longest):
        longest = line
print("Самая длинная строка:", longest)

file = open('resource/text.txt', 'r', encoding='utf-8')
text = file.read()
file.close()

text = text.lower()

glas = 0
soglas = 0

for char in text:
    if char in 'аеёиоуыэюяaeiou':
        glas = glas + 1
    elif char in 'бвгджзйклмнпрстфхцчшщъьbcdfghjklmnpqrstvwxyz':
        soglas = soglas + 1

print("Гласных букв:", glas)
print("Согласных букв:", soglas)