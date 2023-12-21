
from collections import defaultdict

def is_anagram(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())

def if_contains_anagrams(lst):
    anagrams_count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and is_anagram(lst[i], lst[j]):
                anagrams_count += 1
                if anagrams_count > 407:
                    return False
    return True
