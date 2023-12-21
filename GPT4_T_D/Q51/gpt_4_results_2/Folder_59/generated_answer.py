
from collections import Counter

def is_anagram(s1, s2):
    return Counter(s1.lower()) == Counter(s2.lower())

def if_contains_anagrams(lst):
    cnt = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and is_anagram(lst[i], lst[j]):
                cnt += 1
                if cnt > 15:
                    return False
    return True
