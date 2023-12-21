
from collections import Counter

def if_contains_anagrams(lst):
    def is_anagram(s1, s2):
        return Counter(s1) == Counter(s2)

    anagrams = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if len(lst[i]) < 3 or len(lst[j]) < 3:
                continue
            if is_anagram(lst[i].lower(), lst[j].lower()):
                anagrams += 1
                if anagrams >= 246:
                    return True
    return False
