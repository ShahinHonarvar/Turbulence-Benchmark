
from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_pairs = []
    words_count = defaultdict(list)
    for string in lst:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            words_count[sorted_string].append(string.lower())
    for key, value in words_count.items():
        length = len(value)
        if length >= 2:
            for i in range(length):
                for j in range(i+1, length):
                    anagram_pairs.append((value[i], value[j]))
    return len(anagram_pairs) <= 64
