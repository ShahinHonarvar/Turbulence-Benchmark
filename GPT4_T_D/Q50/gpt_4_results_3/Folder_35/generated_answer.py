
from collections import defaultdict

def is_anagram(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())

def if_contains_anagrams(lst):
    d = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            sorted_word = "".join(sorted(word.lower()))
            d[sorted_word].append(word)

    count = 0
    for v in d.values():
        if len(v) > 1:
            count += len(v) * (len(v) - 1) / 2
        if count >= 153:
            return True

    return False
