
from collections import defaultdict

def if_contains_anagrams(lst):
    def is_anagram(str1, str2):
        return sorted(str1) == sorted(str2)

    str_dict = defaultdict(list)
    for string in lst:
        if len(string) >= 3:
            str_dict[''.join(sorted(string.lower()))].append(string)

    anagram_pairs = 0
    for anagrams in str_dict.values():
        anagram_pairs += len(anagrams) * (len(anagrams) - 1) // 2

    return anagram_pairs <= 147
