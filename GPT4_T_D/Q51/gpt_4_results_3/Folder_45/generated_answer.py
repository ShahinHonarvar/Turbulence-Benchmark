
from collections import defaultdict

def if_contains_anagrams(lst):
    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    valid_pairs = 0
    length = len(lst)
    for i in range(length-1):
        for j in range(i+1, length):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                if is_anagram(lst[i], lst[j]):
                    valid_pairs += 1
                    if valid_pairs > 464:
                        return False
    return True
