
from collections import Counter

def if_contains_anagrams(strings):
    pairs = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                s1 = strings[i].lower()
                s2 = strings[j].lower()
                if Counter(s1) == Counter(s2):
                    pairs += 1
                    if pairs > 11:
                        return False
    return True
