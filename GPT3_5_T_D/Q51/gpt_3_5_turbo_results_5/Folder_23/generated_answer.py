 
from itertools import combinations

def if_contains_anagrams(lst):
    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())

    count = 0
    for pair in combinations(lst, 2):
        if len(pair[0]) >= 3 and len(pair[1]) >= 3 and is_anagram(pair[0], pair[1]):
            count += 1
            if count > 49:
                return False

    return True
