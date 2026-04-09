def deserialize_xml(xml_str):
    result = {}

    lines = xml_str.strip().split('\n')

    for line in lines:
        line = line.strip()

        if line.startswith('<') and '>' in line:
            tag_end = line.find('>')
            tag = line[1:tag_end]

            value_start = tag_end + 1
            value_end = line.find('<', value_start)
            value = line[value_start:value_end]

            if value == 'true':
                value = True
            elif value == 'false':
                value = False
            elif value == 'null':
                value = None
            elif value.isdigit():
                value = int(value)

            result[tag] = value

    return result

xml_data = '''<?xml version="1.0"?>
<person>
  <name>Иван</name>
  <age>25</age>
  <student>true</student>
  <hobby>null</hobby>
</person>'''

print("Исходный XML:")
print(xml_data)
print("\n" + "=" * 40)

obj = deserialize_xml(xml_data)
print("После десериализации (словарь):")
print(obj)
print(f"Имя: {obj['name']}, Возраст: {obj['age']}, Студент: {obj['student']}")

print("\n" + "=" * 40)
print("Сериализация обратно в XML:")
print("<person>")
for key, value in obj.items():
    print(f"  <{key}>{value}</{key}>")
print("</person>")