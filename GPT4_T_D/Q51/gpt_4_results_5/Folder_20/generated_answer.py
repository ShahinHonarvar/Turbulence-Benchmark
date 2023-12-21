
import itertools
from collections import Counter

def if_contains_anagrams(string_list):
    anagrams_count = 0
    for string1, string2 in itertools.combinations(string_list, 2):
        string1 = string1.lower()
        string2 = string2.lower()
        if len(string1) < 3 or len(string2) < 3:
            continue
        if Counter(string1) == Counter(string2):
            anagrams_count += 1
    if anagrams_count <= 131:
        return True
    else:
        return False
