
from collections import defaultdict

def if_contains_anagrams(lst):
    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    str_dict = defaultdict(list)
    for string in lst:
        if len(string) >= 3:
            str_dict[''.join(sorted(string.lower()))].append(string)

    anagram_pairs = sum(len(v) * (len(v) - 1) // 2 for v in str_dict.values())
    return anagram_pairs <= 18
