
from itertools import combinations
from collections import Counter

def if_contains_anagrams(lst):
    def is_anagram(str1, str2):
        return Counter(str1.lower()) == Counter(str2.lower())

    anagram_count = 0
    for str1, str2 in combinations(lst, 2):
        if len(str1) >= 3 and len(str2) >= 3 and is_anagram(str1, str2):
            anagram_count += 1
            if anagram_count >= 78:
                return True
    return False
