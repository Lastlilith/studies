"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    """Находит 10 самых длинных слов с наибольшим количеством уникальных символов"""
    words = []
    with open(file_path, encoding='utf-8') as file:
        for line in file:
            words.extend(line.split())

    def unique_chars_count(word):
        return len(set(word)), len(word)

    words.sort(key=lambda w: (-unique_chars_count(w)
               [0], -unique_chars_count(w)[1]))
    return words[:10]


def get_rarest_char(file_path: str) -> str:
    """Находит самый редкий символ в файле"""
    with open(file_path, encoding='utf-8') as file:
        text = file.read()

    char_counts = {}
    for char in text:
        char_counts[char] = char_counts.get(char, 0) + 1

    min_char = None
    min_count = float('inf')
    for char, count in char_counts.items():
        if count < min_count:
            min_count = count
            min_char = char

    return min_char


def count_punctuation_chars(file_path: str) -> int:
    """Подсчитывает количество знаков препинания в файле"""
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    count = 0
    with open(file_path, encoding='utf-8') as file:
        for line in file:
            for char in line:
                if char in punctuation:
                    count += 1
    return count


def count_non_ascii_chars(file_path: str) -> int:
    """Подсчитывает количество не-ASCII символов в файле"""
    count = 0
    with open(file_path, encoding='utf-8') as file:
        for line in file:
            for char in line:
                if ord(char) > 127:
                    count += 1
    return count


def get_most_common_non_ascii_char(file_path: str) -> str:
    """Находит самый частый не-ASCII символ в файле"""
    char_counts = {}
    with open(file_path, encoding='utf-8') as file:
        for line in file:
            for char in line:
                if ord(char) > 127:
                    char_counts[char] = char_counts.get(char, 0) + 1

    max_char = None
    max_count = 0
    for char, count in char_counts.items():
        if count > max_count:
            max_count = count
            max_char = char

    return max_char
