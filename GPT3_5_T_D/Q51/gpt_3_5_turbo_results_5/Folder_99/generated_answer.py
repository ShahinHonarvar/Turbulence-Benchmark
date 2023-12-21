
from collections import Counter

def if_contains_anagrams(strings):
    count = 0
    for i, s1 in enumerate(strings):
        s1_counter = Counter(s1.lower())
        for s2 in strings[i+1:]:
            if len(s2) >= 3 and Counter(s2.lower()) == s1_counter:
                count += 1
                if count > 93:
                    return False
    return True
