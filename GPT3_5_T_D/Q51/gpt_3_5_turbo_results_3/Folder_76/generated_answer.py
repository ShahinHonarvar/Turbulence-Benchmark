
from collections import Counter
from itertools import combinations

def if_contains_anagrams(lst):
    def is_anagram(str1, str2):
        return Counter(str1.lower()) == Counter(str2.lower())
    
    pairs = 0
    
    for str1, str2 in combinations(lst, 2):
        if len(str1) >= 3 and len(str2) >= 3 and is_anagram(str1, str2):
            pairs += 1
            if pairs > 91:
                return False
    
    return True
