## Лабораторная работа 3 
### Тексты и частоты слов (словарь/множество)
### Задание A 
Функция 1 - нормализация текста
```
import re
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold: 
        text = text.casefold()
    if yo2e: 
        text = text.replace('ё', 'е').replace('Ё', 'Е')
    text = re.sub(r"\s+", " ", text)
    text = text.strip()
    return text
print(normalize("ПрИвЕт\nМИр\t"))
print(normalize("ёжик, Ёлка"))
print(normalize("Hello\r\nWorld"))
print(normalize("  двойные  пробелы  "))
```

![im01.png](/images/lab03/im01.png)

Функция 2 - токенизация
```
import re
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..',))
from lib.text import normalize
def tokenize(text: str) -> list[str]:
    regexp = r"[^\w-]" 
    text = normalize(re.sub(regexp, " ", text))
    return text.split(' ')
print(tokenize("привет мир"))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))
```

![im02.png](/images/lab03/im02.png)

Функция 3 - подсчет частоты слов
```
def count_freq(tokens: list[str]) -> dict[str, int]:
    freq_dict = {}
    if not tokens:
        return {}
    for token in tokens:
        freq_dict[token] = freq_dict.get(token, 0) +1
    return freq_dict

print(count_freq(["a","b","a","c","b","a"]))
print(count_freq(["bb","aa","bb","aa","cc"]))
```

![im03.png](/images/lab03/im03.png)

Функция 4 - топ-N по убыванию частоты 
```
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    if not freq:
        return []
    items = list(freq.items())
    items.sort(key=lambda x: x[0])           
    items.sort(key=lambda x: x[1], reverse=True)  
    return items[:n]

freq1 = {"a": 3, "b": 2, "c": 1}
print(top_n(freq1, 2))
freq2 = {"bb": 2, "aa": 2, "cc": 1}
print(top_n(freq2, 2))
```

![im04.png](/images/lab03/im04.png/)

### Задание B
Функция 1 - подсчет общего количество слов, уникальных, топ-5
```
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..',))
import lib.text as text
string = sys.stdin.readline()
tokenized = text.tokenize(string)
unique_words = text.count_freq(tokenized)
print(f"Всего слов: {len(tokenized)}")
print(f"Уникальных слов: {len(unique_words)}")
n = 5
print(f"Топ-{n}:")
k = text.top_n(unique_words)
for token in k:
    print(token[0] + ":" + str(token[1]))
```

![im05.png](/images/lab03/im05.png)


