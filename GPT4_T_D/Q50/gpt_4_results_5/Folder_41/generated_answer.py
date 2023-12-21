
from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_pairs = 0
    frequency = defaultdict(list)

    for string in lst:
        sorted_str = ''.join(sorted(string.upper()))
        if len(sorted_str) >= 3:
            frequency[sorted_str].append(string)

    for key in frequency:
        if len(frequency[key]) >= 2:
            anagram_pairs += len(frequency[key]) * (len(frequency[key]) - 1) // 2

    if anagram_pairs >= 75:
        return True
    return False
