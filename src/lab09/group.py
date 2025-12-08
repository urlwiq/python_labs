import csv
from pathlib import Path
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__)) 
lab08_dir = os.path.join(os.path.dirname(current_dir), 'lab08')  
sys.path.insert(0, lab08_dir)
from models import Student  


class Group:
    HEADER = ["fio", "birthdate", "group", "gpa"]

    def __init__(self, storage_path):
        self.path = Path(storage_path)
        self.path.parent.mkdir(parents=True, exist_ok=True)  
        self._ensure_storage_exists()

    def _ensure_storage_exists(self):
        if not self.path.exists():
            with self.path.open("w", encoding="utf-8", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(self.HEADER)

    def _read_all(self):
        students = []
        if not self.path.exists():  
            return students
            
        try:
            with self.path.open("r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    try:
                        students.append(
                            Student(
                                fio=row["fio"],
                                birthdate=row["birthdate"],
                                group=row["group"],
                                gpa=float(row["gpa"]),
                            )
                        )
                    except Exception as e:
                        print(f"⚠ Ошибка при создании студента: {e}")
        except Exception as e:
            print(f"⚠ Ошибка при чтении файла: {e}")
        return students
    
        

    def list(self):
        return self._read_all()

    def add(self, student):
        existing_students = self._read_all()
        for existing in existing_students:
            if existing.fio == student.fio:
                raise ValueError(f"Студент с ФИО '{student.fio}' уже существует")
        
        file_exists = self.path.exists()
        with self.path.open("a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if file_exists and self.path.stat().st_size > 0:
                with self.path.open("rb") as check_file:
                    check_file.seek(-1, 2) 
                    last_char = check_file.read(1)
                    if last_char != b'\n':
                        f.write('\n')  
            writer.writerow([
                student.fio,
                student.birthdate,
                student.group,
                student.gpa
            ])

    def find(self, substr):
        substr = substr.lower()
        return [s for s in self._read_all() if substr in s.fio.lower()]

    def remove(self, fio):
        students = self._read_all()
        initial_count = len(students)  
        students = [s for s in students if s.fio != fio]
        
        if len(students) < initial_count:  
            with self.path.open("w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(self.HEADER)
                for s in students:
                    writer.writerow([s.fio, s.birthdate, s.group, s.gpa])
            return True  
        return False

    def update(self, fio: str, **fields):
        students = self._read_all()
        updated = False  

        for student in students:
            if student.fio == fio:
                for key, value in fields.items():
                    setattr(student, key, value)
                updated = True
                break

        if not updated:  
            raise ValueError(f"Студент с ФИО '{fio}' не найден")
        
        with self.path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(self.HEADER)
            for st in students:
                writer.writerow([st.fio, st.birthdate, st.group, st.gpa])
if __name__ == "__main__":
    print("=======================")
    
    g = Group("data/lab09/students.csv")
    initial = g.list()
    print(f"Начало: {len(initial)} студентов")
    
    student_to_add = Student("Попов Артем Эдуардович", "2006-01-01", "NE-01", 4.9)
    
    try:
        g.add(student_to_add)
        print(f"\n✓ ДОБАВЛЕН: {student_to_add.fio}")
    except:
        print(f"\n✗ Уже существует")
    
    if initial:
        student_to_remove = initial[0]
        
        if g.remove(student_to_remove.fio):
            print(f"✓ УДАЛЕН: {student_to_remove.fio}")
        else:
            print(f"✗ Не найден для удаления")
    else:
        print("⚠ Нет студентов для удаления")
    final = g.list()
    print(f"\nИтог: {len(final)} студентов")
    