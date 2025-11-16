## Лабораторная работа 5 
### JSON и конвертации (JSON↔CSV, CSV→XLSX): Техническое задание
### Задание A - JSON ↔ CSV
```
import json
import csv
from pathlib import Path
def json_to_csv(json_path: str, csv_path: str) -> None:
    json_file = Path(json_path)
    if not json_file.exists():
        raise FileNotFoundError(f"JSON файл не найден: {json_path}")
    if json_file.suffix.lower() != '.json':
        raise ValueError(f"Неверный тип файла: ожидается .json, получен {json_file.suffix}")
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"Ошибка декодирования JSON: {e}")
    if not isinstance(data, list):
        raise ValueError("JSON должен содержать список объектов")
    if not data:
        raise ValueError("JSON файл пуст")
    for i, item in enumerate(data):
        if not isinstance(item, dict):
            raise ValueError(f"Элемент {i} должен быть словарем, получен {type(item)}")
    fieldnames = sorted(set().union(*(item.keys() for item in data)))
    try:
        Path(csv_path).parent.mkdir(parents=True, exist_ok=True)  
        
        with open(csv_path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            
            for row in data:
                complete_row = {field: row.get(field, '') for field in fieldnames}
                writer.writerow(complete_row)
                
    except Exception as e:
        raise ValueError(f"Ошибка записи CSV файла: {e}")

def csv_to_json(csv_path: str, json_path: str) -> None:
    csv_file = Path(csv_path)
    if not csv_file.exists():
        raise FileNotFoundError(f"CSV файл не найден: {csv_path}")
    if csv_file.suffix.lower() != '.csv':
        raise ValueError(f"Неверный тип файла: ожидается .csv, получен {csv_file.suffix}")
    
    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            
            if reader.fieldnames is None:
                raise ValueError("CSV файл не содержит заголовка")
            
            data = list(reader)
            
    except Exception as e:
        raise ValueError(f"Ошибка чтения CSV файла: {e}")
    if len(data) == 0:
        raise ValueError("CSV файл пуст или содержит только заголовок")
    try:
        Path(json_path).parent.mkdir(parents=True, exist_ok=True)  # Создание директории если нужно
        
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
    except Exception as e:
        raise ValueError(f"Ошибка записи JSON файла: {e}")

def main():
    try:
        Path("data/out").mkdir(parents=True, exist_ok=True)
        
        json_to_csv("data/samples/people.json", "data/out/people_from_json.csv")
        print("JSON -> CSV: Успешно")
        
        csv_to_json("data/samples/people.csv", "data/out/people_from_csv.json")
        print("CSV -> JSON: Успешно")
    except (FileNotFoundError, ValueError) as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
if __name__ == "__main__":
    main()
```
Создаем директории → data/out если не существует
JSON → CSV → читаем people.json, создаем people_from_json.csv
CSV → JSON → читаем people.csv, создаем people_from_csv.json
Выводим результаты → сообщения об успехе или ошибки

### Задание B - CSV → XLSX
```
import csv
from pathlib import Path

try:
    import openpyxl
    from openpyxl.styles import Font
    from openpyxl.utils import get_column_letter
except ImportError:
    openpyxl = None

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    csv_file = Path(csv_path)
    
    if not csv_file.exists():
        raise FileNotFoundError(f"CSV файл не найден: {csv_path}")
    
    if csv_file.suffix.lower() != '.csv':
        raise ValueError(f"Неверный тип файла: ожидается .csv, получен {csv_file.suffix}")
    
    if openpyxl is None:
        raise ImportError("Не установлена библиотека openpyxl")
    
    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            data = list(reader)
    except Exception as e:
        raise ValueError(f"Ошибка чтения CSV файла: {e}")
    
    if not data:
        raise ValueError("CSV файл пуст")
    
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Sheet1"
    for row_idx, row in enumerate(data, 1):
        for col_idx, value in enumerate(row, 1):
            sheet.cell(row=row_idx, column=col_idx, value=value)
    header_font = Font(bold=True)
    for cell in sheet[1]:
        cell.font = header_font
    for column_cells in sheet.columns:
        length = max(8, *(
            len(str(cell.value)) if cell.value else 0
            for cell in column_cells
        ))
        sheet.column_dimensions[get_column_letter(column_cells[0].column)].width = length + 2
    
    Path(xlsx_path).parent.mkdir(parents=True, exist_ok=True)
    workbook.save(xlsx_path)

def main() -> None:
    try:
        Path("data/out").mkdir(parents=True, exist_ok=True)
        csv_to_xlsx("data/samples/people.csv", "data/out/people.xlsx")
        print("CSV -> XLSX: Успешно")
        
    except (FileNotFoundError, ValueError, ImportError) as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")

if __name__ == "__main__":
    main()
```
Читаем CSV → получаем список строк, каждая строка - список значений
Создаем Excel → новая книга с листом "Sheet1"
Записываем данные → переносим построчно из CSV в Excel
Форматируем → заголовок жирным, настраиваем ширину колонок
Сохраняем → создаем XLSX файл

#### Входные данные
##### people.json
![im01.png](/images/lab05/im01.png)
##### cities.csv
![im02.png](/images/lab05/im02.png)
##### people.csv
![im03.png](/images/lab05/im03.png)
#### Выходные файлы
##### people.xlsx
![im04.png](/images/lab05/im04.png)
##### people_from_json.csv
![im05.png](/images/lab05/im05.png)
##### people_from_csv_.json
![im06.png](/images/lab05/im06.png)