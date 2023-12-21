
from collections import defaultdict

def if_contains_anagrams(str_list):
    anagrams = defaultdict(list)
    for word in str_list:
        if len(word) >= 3:
            anagrams[tuple(sorted(word.lower()))].append(word)
    counter = 0
    for key, value in anagrams.items():
        if len(value) > 1:
            counter += (len(value) * (len(value) - 1)) // 2
    return counter >= 48
