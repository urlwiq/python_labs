import pytest
import json
import csv
import os
from lab05.json_csv import json_to_csv, csv_to_json


class TestJsonToCsv:
    """Тесты для функции json_to_csv"""

    def test_json_to_csv_basic(self, tmp_path):
        """Позитивный сценарий: корректная конвертация JSON → CSV"""
        # Подготовка тестового JSON
        json_data = [
            {"name": "Alice", "age": 25, "city": "Moscow"},
            {"name": "Bob", "age": 30, "city": "SPb"},
        ]

        json_file = tmp_path / "test.json"
        csv_file = tmp_path / "output.csv"

        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(json_data, f)

        # Вызов тестируемой функции
        json_to_csv(str(json_file), str(csv_file))

        # Проверка результата
        assert csv_file.exists()

        with open(csv_file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        # Проверяем количество записей
        assert len(rows) == 2
        # Проверяем набор ключей/заголовков
        assert set(rows[0].keys()) == {"age", "city", "name"}
        # Проверяем данные
        assert rows[0]["name"] == "Alice"
        assert rows[0]["age"] == "25"
        assert rows[0]["city"] == "Moscow"

    def test_json_to_csv_different_keys(self, tmp_path):
        """JSON с разными ключами в объектах"""
        json_data = [
            {"name": "Alice", "city": "Moscow"},
            {"name": "Bob", "country": "Russia", "age": 30},
        ]

        json_file = tmp_path / "test.json"
        csv_file = tmp_path / "output.csv"

        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(json_data, f)

        json_to_csv(str(json_file), str(csv_file))

        with open(csv_file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        # Все ключи должны присутствовать в заголовках
        expected_keys = {"name", "city", "country", "age"}
        assert set(rows[0].keys()) | set(rows[1].keys()) == expected_keys

    def test_json_to_csv_file_not_found(self):
        """Негативный сценарий: файл не существует"""
        with pytest.raises(FileNotFoundError):
            json_to_csv("nonexistent.json", "output.csv")

    def test_json_to_csv_invalid_json(self, tmp_path):
        """Негативный сценарий: некорректный JSON"""
        invalid_json_file = tmp_path / "invalid.json"
        output_file = tmp_path / "output.csv"

        with open(invalid_json_file, "w", encoding="utf-8") as f:
            f.write("{invalid json content")

        with pytest.raises(ValueError):
            json_to_csv(str(invalid_json_file), str(output_file))

    def test_json_to_csv_empty_json(self, tmp_path):
        """Негативный сценарий: пустой JSON файл"""
        empty_file = tmp_path / "empty.json"
        output_file = tmp_path / "output.csv"

        empty_file.write_text("")

        with pytest.raises(ValueError):
            json_to_csv(str(empty_file), str(output_file))


class TestCsvToJson:
    """Тесты для функции csv_to_json"""

    def test_csv_to_json_basic(self, tmp_path):
        """Позитивный сценарий: корректная конвертация CSV → JSON"""
        csv_data = """name,age,city
Alice,25,Moscow
Bob,30,SPb"""

        csv_file = tmp_path / "test.csv"
        json_file = tmp_path / "output.json"

        with open(csv_file, "w", encoding="utf-8") as f:
            f.write(csv_data)

        # Вызов тестируемой функции
        csv_to_json(str(csv_file), str(json_file))

        # Проверка результата
        assert json_file.exists()

        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Проверяем количество записей
        assert len(data) == 2
        # Проверяем набор ключей
        assert set(data[0].keys()) == {"name", "age", "city"}
        # Проверяем данные
        assert data[0] == {"name": "Alice", "age": "25", "city": "Moscow"}
        assert data[1] == {"name": "Bob", "age": "30", "city": "SPb"}

    def test_csv_to_json_empty_cells(self, tmp_path):
        """CSV с пустыми ячейками"""
        csv_data = """name,age,city
Alice,25,
Bob,,SPb"""

        csv_file = tmp_path / "test.csv"
        json_file = tmp_path / "output.json"

        with open(csv_file, "w", encoding="utf-8") as f:
            f.write(csv_data)

        csv_to_json(str(csv_file), str(json_file))

        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Пустые ячейки должны стать None или остаться пустыми
        assert data[0]["city"] in [None, ""]
        assert data[1]["age"] in [None, ""]

    def test_csv_to_json_file_not_found(self):
        """Негативный сценарий: файл не существует"""
        with pytest.raises(FileNotFoundError):
            csv_to_json("nonexistent.csv", "output.json")

    def test_csv_to_json_empty_file(self, tmp_path):
        """Негативный сценарий: пустой CSV файл"""
        empty_file = tmp_path / "empty.csv"
        output_file = tmp_path / "output.json"

        empty_file.write_text("")

        with pytest.raises(ValueError):
            csv_to_json(str(empty_file), str(output_file))


class TestIntegration:
    """Интеграционные тесты"""

    def test_json_csv_json_roundtrip(self, tmp_path):
        """Полный цикл конвертации: JSON → CSV → JSON"""
        original_data = [
            {"name": "Alice", "age": 25, "city": "Moscow"},
            {"name": "Bob", "age": 30, "city": "SPb"},
        ]

        json_file1 = tmp_path / "test1.json"
        csv_file = tmp_path / "test.csv"
        json_file2 = tmp_path / "test2.json"

        # JSON → CSV → JSON
        with open(json_file1, "w", encoding="utf-8") as f:
            json.dump(original_data, f)

        json_to_csv(str(json_file1), str(csv_file))
        csv_to_json(str(csv_file), str(json_file2))

        with open(json_file2, "r", encoding="utf-8") as f:
            final_data = json.load(f)

        # Проверяем, что количество записей совпадает
        assert len(final_data) == len(original_data)
