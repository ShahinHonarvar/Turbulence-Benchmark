
from itertools import combinations
from collections import Counter

def if_contains_anagrams(strings):
    anagram_count = 0

    for i, j in combinations(range(len(strings)), 2):
        string1 = strings[i].lower()
        string2 = strings[j].lower()

        if len(string1) >= 3 and len(string2) >= 3 and Counter(string1) == Counter(string2):
            anagram_count += 1

            if anagram_count >= 69:
                return True
    
    return False
