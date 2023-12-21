
from collections import Counter

def if_contains_anagrams(lst):
    anagram_dict = {}
    for string in lst:
        string = string.lower()
        if len(string) >= 3:
            key = "".join(sorted(string))
            if key in anagram_dict:
                anagram_dict[key].append(string)
            else:
                anagram_dict[key] = [string]

    anagram_pairs = 0
    for key, value in anagram_dict.items():
        if len(value) > 1:
            anagram_pairs += len(value) * (len(value) - 1) // 2

    return anagram_pairs >= 194
