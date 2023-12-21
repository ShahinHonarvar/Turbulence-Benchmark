
from collections import Counter

def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)

def if_contains_anagrams(lst):
    anagrams_count = 0
    lst = [''.join(filter(str.isalpha, s)).lower() for s in lst] 
    lst = [s for s in lst if len(s) >= 3]
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if is_anagram(lst[i], lst[j]):
                anagrams_count += 1
            if anagrams_count > 35:
                return False
    return True
