### Задание A - Student (models.py)
```
from dataclasses import dataclass
from datetime import datetime, date
import re
@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Дата должна быть в формате YYYY-MM-DD")
        
        if not (0 <= self.gpa <= 5):
            raise ValueError("GPA должен быть в диапазоне от 0 до 5")
        
        if not re.match(r'^[A-Z]{2}-\d{2}$', self.group):
            raise ValueError("Группа должна быть в формате 'XX-00'")

    def age(self) -> int:
        birth_date = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today()
        age = today.year - birth_date.year
        if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
            age -= 1
        return age

    def to_dict(self) -> dict:
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            fio=data["fio"],
            birthdate=data["birthdate"],
            group=data["group"],
            gpa=data["gpa"]
        )

    def __str__(self):
        return f"Студент: {self.fio}, Группа: {self.group}, GPA: {self.gpa}, Возраст: {self.age()} лет"
```
### Задание B - serialize.py
```
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
    print("==============================")
    
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
```
**Скриншоты выполненных преобразований:**
![im01.png](/images/lab08/im01.png)

![im02.png](/images/lab08/im02.png)