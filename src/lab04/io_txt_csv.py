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