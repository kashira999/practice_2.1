def serialize(obj, indent=0):
    if isinstance(obj, dict):
        items = []
        for k, v in obj.items():
            if isinstance(v, str):
                items.append(f'  "{k}": "{v}"')
            elif isinstance(v, (int, float)):
                items.append(f'  "{k}": {v}')
            elif isinstance(v, bool):
                items.append(f'  "{k}": {str(v).lower()}')
            elif v is None:
                items.append(f'  "{k}": null')
        return "{\n" + ",\n".join(items) + "\n}"
    return str(obj)


def deserialize(json_str):
    result = {}
    lines = json_str.strip().strip('{}').split('\n')

    for line in lines:
        line = line.strip()
        if ':' in line and line:
            key, value = line.split(':', 1)
            key = key.strip().strip('"')
            value = value.strip().strip('"')

            if value == 'true':
                value = True
            elif value == 'false':
                value = False
            elif value == 'null':
                value = None
            elif value.isdigit():
                value = int(value)

            result[key] = value
    return result


def validate(json_str):
    lines = json_str.split('\n')
    for i, line in enumerate(lines, 1):
        line = line.strip()
        if line and line[0] not in '{' and ':' not in line and line[-1] not in '}':
            print(f"Ошибка на строке {i}: {line}")
            return False
    print("JSON валидный!")
    return True


data = {
    "имя": "Иван",
    "возраст": 25,
    "студент": True,
    "хобби": None
}

json_text = serialize(data)
print("СЕРИАЛИЗАЦИЯ:")
print(json_text)

print("\nВАЛИДАЦИЯ:")
validate(json_text)

print("\nДЕСЕРИАЛИЗАЦИЯ:")
obj = deserialize(json_text)
print(obj)
print(f"Имя: {obj['имя']}, Возраст: {obj['возраст']}")