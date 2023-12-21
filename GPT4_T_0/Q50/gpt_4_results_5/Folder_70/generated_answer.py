
from collections import Counter

def if_contains_anagrams(lst):
    def is_anagram(s1, s2):
        return Counter(s1) == Counter(s2)

    anagram_pairs = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and is_anagram(lst[i].lower(), lst[j].lower()):
                anagram_pairs += 1
                if anagram_pairs >= 189:
                    return True
    return False
