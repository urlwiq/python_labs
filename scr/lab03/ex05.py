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