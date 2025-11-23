### Задание A - Тесты для src/lib/text.py
```
import pytest
from lib.io_helpers import normalize, tokenize, count_freq, top_n


@pytest.mark.parametrize(
    "source, expected",
    [
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\r\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
        ("", ""),
        ("   ", ""),
    ],
)
def test_normalize(source, expected):
    assert normalize(source) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("привет мир", ["привет", "мир"]),
        ("hello world test", ["hello", "world", "test"]),
        ("", []),
        ("   ", []),
        ("знаки, препинания! тест.", ["знаки", "препинания", "тест"]),
    ],
)
def test_tokenize(text, expected):
    assert tokenize(text) == expected


def test_count_freq_basic():
    tokens = ["apple", "banana", "apple", "cherry", "banana", "apple"]
    result = count_freq(tokens)
    expected = {"apple": 3, "banana": 2, "cherry": 1}
    assert result == expected


def test_count_freq_empty():
    assert count_freq([]) == {}


def test_top_n_basic():
    freq = {"apple": 5, "banana": 3, "cherry": 7, "date": 1}
    result = top_n(freq, 2)
    expected = [("cherry", 7), ("apple", 5)]
    assert result == expected


def test_top_n_tie_breaker():
    freq = {"banana": 3, "apple": 3, "cherry": 3}
    result = top_n(freq, 3)
    expected = [("apple", 3), ("banana", 3), ("cherry", 3)]
    assert result == expected


def test_top_n_empty():
    assert top_n({}, 5) == []


def test_full_pipeline():
    text = "Привет мир! Привет всем. Мир прекрасен."
    normalized = normalize(text)
    tokens = tokenize(normalized)
    freq = count_freq(tokens)
    top_words = top_n(freq, 2)

    assert normalized == "привет мир! привет всем. мир прекрасен."
    assert tokens == [
        "привет",
        "мир",
        "привет",
        "всем",
        "мир",
        "прекрасен",
    ]
    assert freq == {"привет": 2, "мир": 2, "всем": 1, "прекрасен": 1}
    assert top_words == [("мир", 2), ("привет", 2)]
```
### Задание B -  Тесты для src/lab05/json_csv.py
```

import pytest
import json
import csv
import os
from lab05.json_csv import json_to_csv, csv_to_json


class TestJsonToCsv:
    def test_json_to_csv_basic(self, tmp_path):
        json_data = [
            {"name": "Alice", "age": 25, "city": "Moscow"},
            {"name": "Bob", "age": 30, "city": "SPb"}
        ]
        json_file = tmp_path / "test.json"
        csv_file = tmp_path / "output.csv"
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(json_data, f)
        json_to_csv(str(json_file), str(csv_file))
        assert csv_file.exists()
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        assert len(rows) == 2
        assert set(rows[0].keys()) == {"age", "city", "name"}
        assert rows[0]["name"] == "Alice"
        assert rows[0]["age"] == "25"
        assert rows[0]["city"] == "Moscow"
    
    def test_json_to_csv_different_keys(self, tmp_path):
        json_data = [
            {"name": "Alice", "city": "Moscow"},
            {"name": "Bob", "country": "Russia", "age": 30}
        ]
        
        json_file = tmp_path / "test.json"
        csv_file = tmp_path / "output.csv"
        
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(json_data, f)
        
        json_to_csv(str(json_file), str(csv_file))
        
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        
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
        
        with open(invalid_json_file, 'w', encoding='utf-8') as f:
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
        with open(csv_file, 'w', encoding='utf-8') as f:
            f.write(csv_data)
        csv_to_json(str(csv_file), str(json_file))
        assert json_file.exists()
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        assert len(data) == 2
        assert set(data[0].keys()) == {"name", "age", "city"}
        assert data[0] == {"name": "Alice", "age": "25", "city": "Moscow"}
        assert data[1] == {"name": "Bob", "age": "30", "city": "SPb"}
    
    def test_csv_to_json_empty_cells(self, tmp_path):
        """CSV с пустыми ячейками"""
        csv_data = """name,age,city
Alice,25,
Bob,,SPb"""
        
        csv_file = tmp_path / "test.csv"
        json_file = tmp_path / "output.json"
        with open(csv_file, 'w', encoding='utf-8') as f:
            f.write(csv_data)
        csv_to_json(str(csv_file), str(json_file))
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        assert data[0]["city"] in [None, ""]
        assert data[1]["age"] in [None, ""]
    
    def test_csv_to_json_file_not_found(self):
        with pytest.raises(FileNotFoundError):
            csv_to_json("nonexistent.csv", "output.json")
    
    def test_csv_to_json_empty_file(self, tmp_path):
        empty_file = tmp_path / "empty.csv"
        output_file = tmp_path / "output.json"
        empty_file.write_text("")
        with pytest.raises(ValueError):
            csv_to_json(str(empty_file), str(output_file))


class TestIntegration:
    def test_json_csv_json_roundtrip(self, tmp_path):
        original_data = [
            {"name": "Alice", "age": 25, "city": "Moscow"},
            {"name": "Bob", "age": 30, "city": "SPb"}
        ]
        json_file1 = tmp_path / "test1.json"
        csv_file = tmp_path / "test.csv"
        json_file2 = tmp_path / "test2.json"
        
        with open(json_file1, 'w', encoding='utf-8') as f:
            json.dump(original_data, f)
        json_to_csv(str(json_file1), str(csv_file))
        csv_to_json(str(csv_file), str(json_file2))
        with open(json_file2, 'r', encoding='utf-8') as f:
            final_data = json.load(f)
        assert len(final_data) == len(original_data)
```

## Выполненные тесты 
![im01.png](/images/lab07/im01.png)

## Стиль кода
![im02.png](/images/lab07/im02.png)
![im03.png](/images/lab07/im03.png)