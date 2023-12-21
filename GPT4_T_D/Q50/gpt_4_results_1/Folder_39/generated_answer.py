
from collections import Counter

def if_contains_anagrams(lst):
    str_dict = {}

    for word in lst:
        char_count = Counter(word.lower())
        if len(char_count) >= 3:
            char_count = tuple(sorted(char_count.items(), key=lambda x: x[0]))
            str_dict[char_count] = str_dict.get(char_count, 0) + 1

    anagram_count = sum([value * (value - 1) // 2 for value in str_dict.values()])

    return anagram_count >= 54
