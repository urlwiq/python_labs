import json
import csv
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:
    json_file = Path(json_path)
    if not json_file.exists():
        raise FileNotFoundError(f"JSON файл не найден: {json_path}")
    if json_file.suffix.lower() != ".json":
        raise ValueError(
            f"Неверный тип файла: ожидается .json, получен {json_file.suffix}"
        )
    try:
        with open(json_path, "r", encoding="utf-8") as f:
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

        with open(csv_path, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()

            for row in data:
                complete_row = {field: row.get(field, "") for field in fieldnames}
                writer.writerow(complete_row)

    except Exception as e:
        raise ValueError(f"Ошибка записи CSV файла: {e}")


def csv_to_json(csv_path: str, json_path: str) -> None:
    csv_file = Path(csv_path)
    if not csv_file.exists():
        raise FileNotFoundError(f"CSV файл не найден: {csv_path}")
    if csv_file.suffix.lower() != ".csv":
        raise ValueError(
            f"Неверный тип файла: ожидается .csv, получен {csv_file.suffix}"
        )

    try:
        with open(csv_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            if reader.fieldnames is None:
                raise ValueError("CSV файл не содержит заголовка")

            data = list(reader)

    except Exception as e:
        raise ValueError(f"Ошибка чтения CSV файла: {e}")
    if len(data) == 0:
        raise ValueError("CSV файл пуст или содержит только заголовок")
    try:
        Path(json_path).parent.mkdir(
            parents=True, exist_ok=True
        )  # Создание директории если нужно

        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    except Exception as e:
        raise ValueError(f"Ошибка записи JSON файла: {e}")


def main() -> None:
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
