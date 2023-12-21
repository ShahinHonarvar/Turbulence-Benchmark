
from collections import Counter

def is_anagram_str(a, b):
    return Counter(a) == Counter(b)

def if_contains_anagrams(lst):
    pairs = 0
    n = len(lst)
    for i in range(n):
        for j in range(i+1, n):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and is_anagram_str(lst[i].lower(), lst[j].lower()):
                pairs += 1
                if pairs == 93:
                    return True
    return False
