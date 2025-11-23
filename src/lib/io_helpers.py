import re
from typing import Dict, List, Tuple
from collections import Counter
from pathlib import Path
from typing import Union


def normalize(text: str) -> str:
    """Приводит текст к нижнему регистру и удаляет знаки препинания."""
    if not text:
        return ""

    # Приводим к нижнему регистру
    result = text.lower()

    # Заменяем ё на е
    result = result.replace("ё", "е")

    # УДАЛЯЕМ ВСЕ знаки препинания
    import string

    punctuation_chars = string.punctuation + "«»—"

    # Заменяем все знаки препинания на пробелы
    for char in punctuation_chars:
        result = result.replace(char, " ")

    # Также заменяем специальные символы на пробелы
    for char in ["\t", "\r", "\n"]:
        result = result.replace(char, " ")

    # Убираем лишние пробелы
    result = re.sub(r"\s+", " ", result).strip()

    return result


def tokenize(text: str) -> List[str]:
    """Разбивает текст на слова (токены)."""
    if not text:
        return []

    # Нормализуем текст
    normalized = normalize(text)
    if not normalized:
        return []

    # РАЗБИВАЕМ слова с дефисами на отдельные слова
    words = []
    for word in normalized.split():
        # Если слово содержит дефис, разбиваем его
        if "-" in word:
            parts = word.split("-")
            words.extend(parts)
        else:
            words.append(word)

    # Фильтруем пустые строки и возвращаем
    return [word for word in words if word]


def count_freq(tokens: List[str]) -> Dict[str, int]:
    """Подсчитывает частоту слов."""
    freq = {}
    for token in tokens:
        # Убедимся, что всё в нижнем регистре
        token_clean = token.lower().strip()
        if token_clean:
            freq[token_clean] = freq.get(token_clean, 0) + 1
    return freq


def top_n(freq: Dict[str, int], n: int) -> List[Tuple[str, int]]:
    """Возвращает n самых частых слов."""
    # ИСПРАВЛЯЕМ: если n <= 0, возвращаем пустой список
    if not freq or n <= 0:
        return []

    items = list(freq.items())
    sorted_items = sorted(items, key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]


def ensure_parent_dir(path: Union[str, Path]):
    """Создает родительскую директорию для пути."""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    test_text = "Привет, мир! Привет!!! Тест-тест проверка."
    print("Исходный текст:", test_text)

    norm_text = normalize(test_text)
    print("Нормализованный:", norm_text)

    tokens = tokenize(test_text)
    print("Токены:", tokens)

    freq = count_freq(tokens)
    print("Частоты:", freq)

    top_3 = top_n(freq, 3)
    print("Топ-3:", top_3)
