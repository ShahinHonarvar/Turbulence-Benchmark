
from collections import Counter

def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)

def if_contains_anagrams(lst):
    num_anagrams = 0

    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                if is_anagram(lst[i].lower(), lst[j].lower()):
                    num_anagrams += 1
                    if num_anagrams >= 59:
                        return True
    return False
