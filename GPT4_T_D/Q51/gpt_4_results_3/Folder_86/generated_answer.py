
from collections import defaultdict

def is_anagram(str1, str2):
    if len(str1) != len(str2) or len(str1) < 3:
        return False
    str1, str2 = str1.lower(), str2.lower()
    return sorted(str1) == sorted(str2)

def if_contains_anagrams(strings):
    anagrams_dict = defaultdict(list)
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        anagrams_dict[sorted_string].append(string)
    num_anagram_pairs = sum(len(vals)*(len(vals)-1)//2 for vals in anagrams_dict.values())
    return num_anagram_pairs <= 48
