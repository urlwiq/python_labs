import json
from models import Student

def students_to_json(students: list[Student], path: str):
    data = [student.to_dict() for student in students]
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def students_from_json(path: str) -> list[Student]:
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    students = []
    for item in data:
        try:
            student = Student.from_dict(item)
            students.append(student)
        except (ValueError, KeyError) as e:
            print(f"Ошибка при создании студента: {e}")
    return students
def demo_serialization():
    print("=========================")
    input_path = "data/lab08/students_input.json"
    output_path = "data/lab08/students_output.json"
    try:
        students = students_from_json(input_path)
        print(f"Загружено студентов: {len(students)}")
        students_to_json(students, output_path)
        print("JSON файл создан")
        print("✓ Сериализация завершена успешно!")
        
    except Exception as e:
        print(f"✗ Ошибка: {e}")
if __name__ == "__main__":
    demo_serialization()