
from collections import Counter

def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)

def if_contains_anagrams(lst):
    anagram_pairs = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if len(lst[i]) > 2 and len(lst[j]) > 2 and is_anagram(lst[i].lower(), lst[j].lower()):
                anagram_pairs += 1
                if anagram_pairs > 92:
                    return False
    return True
