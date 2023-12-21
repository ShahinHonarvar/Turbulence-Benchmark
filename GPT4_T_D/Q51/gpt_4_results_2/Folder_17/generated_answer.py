
from collections import defaultdict

def if_contains_anagrams(lst):
    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    n = len(lst)
    pairs = 0
    for i in range(n):
        for j in range(i+1, n):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and is_anagram(lst[i], lst[j]):
                pairs += 1
                if pairs > 22:
                    return False
    return True
