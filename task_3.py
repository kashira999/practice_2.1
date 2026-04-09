file = open('resource/products.csv', 'r', encoding='utf-8')
lines = file.readlines()
file.close()

products = []
for i in range(1, len(lines)):
    parts = lines[i].strip().split(',')
    products.append([parts[0], int(parts[1]), int(parts[2])])

while True:
    print("\n1 - Все товары")
    print("2 - Добавить товар")
    print("3 - Найти товар")
    print("4 - Общая стоимость")
    print("5 - Сохранить отсортированные по цене")
    print("6 - Выйти")

    choice = input("Выберите: ")

    if choice == "1":
        print("\nНазвание\tЦена\tКол-во")
        for p in products:
            print(p[0] + "\t\t" + str(p[1]) + "\t" + str(p[2]))

    elif choice == "2":
        name = input("Название: ")
        price = int(input("Цена: "))
        count = int(input("Количество: "))
        products.append([name, price, count])
        print("Добавлено!")

    elif choice == "3":
        name = input("Название для поиска: ")
        found = False
        for p in products:
            if p[0].lower() == name.lower():
                print("Найдено:", p[0], p[1], p[2])
                found = True
                break
        if not found:
            print("Не найдено")

    elif choice == "4":
        total = 0
        for p in products:
            total = total + p[1] * p[2]
        print("Общая стоимость:", total, "руб")

    elif choice == "5":
        sorted_products = []
        for p in products:
            sorted_products.append([p[0], p[1], p[2]])

        for i in range(len(sorted_products)):
            for j in range(i + 1, len(sorted_products)):
                if sorted_products[i][1] > sorted_products[j][1]:
                    sorted_products[i], sorted_products[j] = sorted_products[j], sorted_products[i]

        file = open('resource/sorted_products.csv', 'w', encoding='utf-8')
        file.write("Название,Цена,Количество\n")
        for p in sorted_products:
            file.write(p[0] + "," + str(p[1]) + "," + str(p[2]) + "\n")
        file.close()
        print("Отсортированные продукты сохранены в sorted_products.csv")

    elif choice == "6":
        file = open('resource/products.csv', 'w', encoding='utf-8')
        file.write("Название,Цена,Количество\n")
        for p in products:
            file.write(p[0] + "," + str(p[1]) + "," + str(p[2]) + "\n")
        file.close()
        print("До свидания!")
        break