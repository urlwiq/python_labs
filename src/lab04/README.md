## Лабораторная работа 4
### Файлы: TXT/CSV и отчёты по текстовой статистике
### Задание А 
Функция 1 - чтение текста
```
from csv import writer
from pathlib import Path
import csv
from typing import Iterable, Sequence

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path)
    return p.read_text(encoding=encoding)
def write_csv(rows: Iterable[Sequence], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    p = Path(path)
    rows = list(rows)
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)
from collections import Counter
def frequencies_from_text(text: str) -> dict[str, int]:
    from lib.text import normalize, tokenize  
    tokens = tokenize(normalize(text))
    return Counter(tokens)  
def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))
def ensure_parent_dir(path: str | Path) -> None:
        parent_directory = Path(path).parent
        parent_directory.mkdir(parents=True, exist_ok=True)
```
Функция 2 - запись текста
```
import csv
import sys
from pathlib import Path
import os

sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.append(os.path.join(os.path.dirname(__file__), '..',))
from lab04.io_txt_csv import read_text, write_csv
from lib.text import normalize, tokenize, count_freq, top_n

def main():
    input_file = "scr/data/lab04/input.txt"  
    output_file = "scr/data/lab04/report.csv"  
    
    try:
        text = read_text(input_file)
        freq = count_freq(tokenize(normalize(text)))
        write_csv(sorted(freq.items(), key=lambda x: (-x[1], x[0])), 
                 output_file, header=("word", "count"))
        
        print(f"✓ Отчёт сохранён: {output_file}")
        print(f"Всего слов: {sum(freq.values())}")
        print(f"Уникальных слов: {len(freq)}")
        print("Топ-5:", *[f"{w}:{c}" for w, c in top_n(freq, 5)])
        
    except FileNotFoundError:
        print(f"✗ Файл {input_file} не найден")
        sys.exit(1)
    except Exception as e:
        print(f"✗ Ошибка: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

![im01.png](/images/lab04/im01.png)
