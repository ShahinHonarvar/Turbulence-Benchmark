
from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagram_dict[sorted_string].append(string)
    count = sum(len(values) * (len(values) - 1) // 2 for values in anagram_dict.values())
    return count >= 15
