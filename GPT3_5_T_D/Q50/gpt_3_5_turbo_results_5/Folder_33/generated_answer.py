
from collections import Counter

def if_contains_anagrams(strings):
    count = 0
    for index, s1 in enumerate(strings):
        c1 = Counter(s1.lower())
        for s2 in strings[index+1:]:
            c2 = Counter(s2.lower())
            if c1 == c2 and len(s1) >= 3:
                count += 1
                if count >= 140:
                    return True
    return False
