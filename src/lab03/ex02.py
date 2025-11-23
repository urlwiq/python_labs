import re
import sys
import os

sys.path.append(
    os.path.join(
        os.path.dirname(__file__),
        "..",
    )
)
from lib.text import normalize


def tokenize(text: str) -> list[str]:
    regexp = r"[^\w-]"
    text = normalize(re.sub(regexp, " ", text))
    return text.split(" ")


print(tokenize("привет мир"))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))
