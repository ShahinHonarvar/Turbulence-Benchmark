
from collections import Counter

def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)

def if_contains_anagrams(lst):
    anagram_count = 0
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and is_anagram(lst[i].lower(), lst[j].lower()):
                anagram_count += 1
            if anagram_count >= 40:
                return True
    return False
