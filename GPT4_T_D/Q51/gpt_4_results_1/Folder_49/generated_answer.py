
from collections import defaultdict

def if_contains_anagrams(lst):
    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    anagram_count = 0
    length = len(lst)
    
    for i in range(length):
        if len(lst[i]) < 3:
            continue
        for j in range(i+1, length):
            if len(lst[j]) < 3:
                continue
            if is_anagram(lst[i], lst[j]):
                anagram_count += 1
                if anagram_count > 10:
                    return False
    return True
