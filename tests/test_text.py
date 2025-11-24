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
        ("программирование python", ["программирование", "python"]),
        ("java script python", ["java", "script", "python"]),
        ("", []),
        ("       ", []),
        ("разные, знаки! препинания.", ["разные", "знаки", "препинания"]),
    ],
)
def test_tokenize(text, expected):
    assert tokenize(text) == expected


def test_count_freq_basic():
    tokens = ["python", "java", "python", "c++", "java", "python"]
    result = count_freq(tokens)
    expected = {"python": 3, "java": 2, "c++": 1}
    assert result == expected


def test_count_freq_empty():
    assert count_freq([]) == {}


def test_top_n_basic():
    freq = {"python": 8, "java": 5, "javascript": 12, "go": 2}
    result = top_n(freq, 2)
    expected = [("javascript", 12), ("python", 8)]
    assert result == expected


def test_top_n_tie_breaker():
    freq = {"ruby": 4, "php": 4, "swift": 4}
    result = top_n(freq, 3)
    expected = [("php", 4), ("ruby", 4), ("swift", 4)]
    assert result == expected


def test_top_n_empty():
    assert top_n({}, 3) == []


def test_full_pipeline():
    text = "Программирование Python! Программирование интересно. Python мощный."
    normalized = normalize(text)
    tokens = tokenize(normalized)
    freq = count_freq(tokens)
    top_words = top_n(freq, 2)

    assert normalized == "программирование python! программирование интересно. python мощный."
    assert tokens == [
        "программирование",
        "python",
        "программирование",
        "интересно",
        "python",
        "мощный",
    ]
    assert freq == {"программирование": 2, "python": 2, "интересно": 1, "мощный": 1}
    assert top_words == [("python", 2), ("программирование", 2)]