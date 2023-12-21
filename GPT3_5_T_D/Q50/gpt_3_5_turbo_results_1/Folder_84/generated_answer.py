
from itertools import combinations
from collections import Counter

def if_contains_anagrams(string_list):
    anagram_pairs = 0
    for i, j in combinations(range(len(string_list)), 2):
        if len(string_list[i]) >= 3 and len(string_list[j]) >= 3:
            if Counter(string_list[i].lower()) == Counter(string_list[j].lower()):
                anagram_pairs += 1
                if anagram_pairs >= 108:
                    return True
    return False
