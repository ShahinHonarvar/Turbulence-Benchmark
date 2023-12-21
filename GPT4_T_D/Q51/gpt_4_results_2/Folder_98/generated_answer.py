
from collections import Counter

def if_contains_anagrams(lst):
    def is_anagram(s1, s2):
        return Counter(s1.lower()) == Counter(s2.lower())
    
    pairs = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) > 2 and len(lst[j]) > 2 and is_anagram(lst[i], lst[j]):
                pairs += 1
                if pairs > 46:
                    return False
    return True
