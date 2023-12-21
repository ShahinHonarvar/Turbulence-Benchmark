
from collections import Counter

def if_contains_anagrams(lst):
    def is_anagram(s1, s2):
        if len(s1) < 3 or len(s2) < 3:
            return False
        return Counter(s1) == Counter(s2)

    pair_count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if is_anagram(lst[i].lower(), lst[j].lower()):
                pair_count += 1
                if pair_count > 38:
                    return False
    return True
