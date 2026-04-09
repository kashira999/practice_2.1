key = int(input("Введите ключ (0-255): "))
name = input("Имя файла: ")

f = open(name, 'rb')
data = f.read()
f.close()

res = bytearray()
for b in data:
    b = ((b << 2) | (b >> 6)) & 0xFF
    b = b ^ key
    res.append(b)

f = open('зашифровано_' + name, 'wb')
f.write(res)
f.close()

print("Готово! Файл: зашифровано_" + name)
print("\nЧтобы расшифровать, запустите программу снова и выберите расшифровку")

choice = input("\nРасшифровать? (да/нет): ")
if choice == 'да':
    f = open('зашифровано_' + name, 'rb')
    data = f.read()
    f.close()

    res2 = bytearray()
    for b in data:
        b = b ^ key
        b = ((b >> 2) | (b << 6)) & 0xFF
        res2.append(b)

    f = open('расшифровано_' + name, 'wb')
    f.write(res2)
    f.close()
    print("Расшифровано! Файл: расшифровано_" + name)