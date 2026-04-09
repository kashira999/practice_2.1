import json

try:
    f = open('resource/library.json', 'r', encoding='utf-8')
    books = json.load(f)
    f.close()
except:
    books = []


def save():
    f = open('resource/library.json', 'w', encoding='utf-8')
    json.dump(books, f, ensure_ascii=False, indent=2)
    f.close()


while True:
    print("\n1-Все 2-Поиск 3-Добавить 4-Статус 5-Удалить 6-Экспорт 7-Выход")
    choice = input("Выберите: ")

    if choice == '1':
        for b in books:
            status = "доступна" if b['available'] else "взята"
            print(f"{b['id']}: {b['title']} - {b['author']} ({status})")

    elif choice == '2':
        word = input("Поиск: ").lower()
        for b in books:
            if word in b['title'].lower() or word in b['author'].lower():
                print(f"{b['title']} - {b['author']}")

    elif choice == '3':
        new_id = max([b['id'] for b in books]) + 1 if books else 1
        books.append({
            'id': new_id,
            'title': input("Название: "),
            'author': input("Автор: "),
            'year': input("Год: "),
            'available': True
        })
        save()
        print("Добавлено!")

    elif choice == '4':
        id = int(input("ID книги: "))
        for b in books:
            if b['id'] == id:
                b['available'] = not b['available']
                save()
                print("Статус изменен")
                break

    elif choice == '5':
        id = int(input("ID для удаления: "))
        for i in range(len(books)):
            if books[i]['id'] == id:
                books.pop(i)
                save()
                print("Удалено")
                break

    elif choice == '6':
        f = open('available_books.txt', 'w', encoding='utf-8')
        f.write("Доступные книги:\n")
        for b in books:
            if b['available']:
                f.write(f"{b['title']} - {b['author']}\n")
        f.close()
        print("Экспортировано!")

    elif choice == '7':
        break