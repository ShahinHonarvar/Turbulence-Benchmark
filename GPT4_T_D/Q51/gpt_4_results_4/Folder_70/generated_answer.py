
from collections import defaultdict

def is_anagram(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())

def if_contains_anagrams(str_list):
    n = len(str_list)
    dictionary = defaultdict(list)
    for word in str_list:
        if len(word) >= 3:
            dictionary["".join(sorted(word.lower()))].append(word)
    pairs = sum(len(values) * (len(values) - 1) // 2 for values in dictionary.values())
    return pairs <= 97
