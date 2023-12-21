
from collections import Counter

def is_anagram(s1, s2):
    return Counter(s1.lower()) == Counter(s2.lower())

def if_contains_anagrams(lst):
    lst = [s for s in lst if len(s) >= 3]
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if is_anagram(lst[i], lst[j]):
                count += 1
                if count == 21:
                    return True
    return False
