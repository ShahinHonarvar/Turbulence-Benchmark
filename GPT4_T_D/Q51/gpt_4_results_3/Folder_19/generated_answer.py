
from collections import Counter
from itertools import combinations

def if_contains_anagrams(lst):
    def is_anagram(str1, str2):
        return Counter(str1.lower()) == Counter(str2.lower())
    
    anagram_pairs = 0
    for pair in combinations(lst, 2):
        str1, str2 = pair
        if len(str1) >= 3 and len(str2) >= 3 and is_anagram(str1, str2):
            anagram_pairs += 1
            if anagram_pairs > 69:
                return False
    return True
