import struct

filename = input("Введите имя файла: ")

try:
    with open(filename, 'rb') as f:
        sig = f.read(4)
        if sig != b'DATA':
            print("Неверная сигнатура!")
            exit()

        ver = struct.unpack('<H', f.read(2))[0]
        count = struct.unpack('<I', f.read(4))[0]

        temps = []
        active = 0

        for i in range(count):
            ts = struct.unpack('<Q', f.read(8))[0]
            id_num = struct.unpack('<I', f.read(4))[0]
            temp = struct.unpack('<h', f.read(2))[0] / 100
            flag = struct.unpack('<B', f.read(1))[0]

            temps.append(temp)
            if flag & 1:
                active += 1

            print(f"{i + 1}: ID={id_num}, temp={temp:.2f}°C, flag={flag}")

        print(f"\nСредняя температура: {sum(temps) / len(temps):.2f}°C")
        print(f"Активных флагов: {active}")

except FileNotFoundError:
    print("Файл не найден!")
except Exception as e:
    print(f"Ошибка: {e}")