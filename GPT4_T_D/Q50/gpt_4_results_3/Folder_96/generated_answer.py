
from collections import Counter

def if_contains_anagrams(lst):
    anagram_pairs = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) > 2 and len(lst[j]) > 2:  # strings must be at least 3 characters long
                if Counter(lst[i].lower()) == Counter(lst[j].lower()):
                    anagram_pairs += 1
                    if anagram_pairs >= 98:
                        return True
    return False
