
from collections import defaultdict

def is_anagram(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())

def if_contains_anagrams(lst):
    n = len(lst)
    count_anagram_pairs = 0
    for i in range(n):
        for j in range(i+1, n):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and is_anagram(lst[i], lst[j]):
                count_anagram_pairs += 1
                if count_anagram_pairs > 81:
                    return False
    return True
