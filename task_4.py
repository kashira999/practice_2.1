import math
from datetime import datetime

try:
    f = open('resource/calculator.log', 'r')
    lines = f.readlines()
    f.close()
    print("\n--- Последние операции ---")
    for i in range(max(0, len(lines) - 5), len(lines)):
        print(lines[i].strip())
except:
    print("Нет истории")

while True:
    print("\nОперации: + - * / log sin (или 'выход' / 'очистить')")
    op = input("Операция: ")

    if op == 'выход':
        break
    elif op == 'очистить':
        open('resource/calculator.log', 'w').close()
        print("Лог очищен")
        continue

    try:
        if op in ['log', 'sin']:
            x = float(input("Число: "))
            if op == 'log':
                res = math.log(x)
                zap = f"[{datetime.now()}] log({x}) = {res}"
            else:
                res = math.sin(x)
                zap = f"[{datetime.now()}] sin({x}) = {res}"
        else:
            a = float(input("a = "))
            b = float(input("b = "))
            if op == '+':
                res = a + b
            elif op == '-':
                res = a - b
            elif op == '*':
                res = a * b
            elif op == '/':
                res = a / b
            zap = f"[{datetime.now()}] {a} {op} {b} = {res}"

        print("=", res)
        f = open('resource/calculator.log', 'a')
        f.write(zap + "\n")
        f.close()
    except:
        print("Ошибка!")