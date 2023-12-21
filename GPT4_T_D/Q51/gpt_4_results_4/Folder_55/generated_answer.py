
from collections import defaultdict

def if_contains_anagrams(lst):
    def is_anagrams(s1, s2):
        s1 = s1.lower()
        s2 = s2.lower()
        return sorted(s1) == sorted(s2)

    if len(lst) < 2:
        return False
        
    pairs = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            pairs[''.join(sorted(word.lower()))].append(word)

    count = sum(len(value) * (len(value) - 1) // 2 for value in pairs.values())
    return count <= 44
