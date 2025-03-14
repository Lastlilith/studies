"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
import string
import unicodedata
from typing import List, Tuple


def read_and_decode_file(file_path: str) -> str:
    """Читает файл и декодирует Unicode escape последовательности"""
    with open(file_path, "r", encoding="utf-8") as f:
        raw_text = f.read()
    return raw_text.encode().decode("unicode_escape")


def get_longest_diverse_words(text: str) -> List[str]:
    """Находит 10 самых длинных слов с наибольшим количеством уникальных символов"""
    words = text.split()
    clean_words = [word.strip(string.punctuation) for word in words if word]

    def key_func(word):
        return len(set(word)), len(word)

    sorted_words = sorted(clean_words, key=key_func, reverse=True)
    return sorted_words[:10]


def get_rarest_char(text: str) -> str:
    """Находит самый редкий символ в файле"""
    char_counts = {}
    for ch in text:
        char_counts[ch] = char_counts.get(ch, 0) + 1

    return min(char_counts, key=char_counts.get)


def count_punctuation_chars(text: str) -> int:
    """Подсчитывает количество знаков препинания в файле"""
    return sum(1 for ch in text if ch in string.punctuation)


def count_non_ascii_chars(text: str) -> int:
    """Подсчитывает количество не-ASCII символов в файле"""
    return sum(1 for ch in text if ord(ch) > 127)


def get_most_common_non_ascii_char(text: str) -> Tuple[str, int]:
    """Находит самый частый не-ASCII символ в файле"""
    char_counts = {}
    for ch in text:
        if ord(ch) > 127:
            char_counts[ch] = char_counts.get(ch, 0) + 1

    if not char_counts:
        return "Non-ASCII не найдены", 0

    max_char = max(char_counts, key=char_counts.get)
    return max_char, char_counts[max_char]


# Доказательство работоспособности
file_path = "data.txt"
decoded_text = read_and_decode_file(file_path)

test_res = {
    "Longest": ", ".join(get_longest_diverse_words(decoded_text)),
    "Rarest symbol": get_rarest_char(decoded_text),
    "Punctuation сount": str(count_punctuation_chars(decoded_text)),
    "Non-ASCII char сount": str(count_non_ascii_chars(decoded_text)),
    "Most сommon Non-ASCII char": str(get_most_common_non_ascii_char(decoded_text)),
}

for key, value in test_res.items():
    print(f"{key}: {value}")
