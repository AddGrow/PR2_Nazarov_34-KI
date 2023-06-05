import json
import xml.etree.ElementTree as ET

json_file = open("students.json","r")
xml_file = open("students.xml","r")

json_data = json.load(json_file)
xml_data = ET.parse(xml_file)

json_file.close()
xml_file.close()

students = []

for student in json_data["students"]:
    students.append(student)

for student in xml_data.findall("student"):
    students.append({
        "name": student.find("name").text,
        "surname": student.find("surname").text,
        "group": student.find("group").text,
        "estimates": {
            "module_1": student.find("estimates/module_1").text,
            "module_2": student.find("estimates/module_2").text,
            "module_3": student.find("estimates/module_3").text
        }
    })

print("| Ім'я | Прізвище | Група | Модуль 1 | Модуль 2 | Модуль 3 |")

for student in students:
    print("| {0} | {1} | {2} | {3} | {4} | {5} |".format(
        student["name"],
        student["surname"],
        student["group"],
        student["estimates"]["module_1"],
        student["estimates"]["module_2"],
        student["estimates"]["module_3"],
    ))
