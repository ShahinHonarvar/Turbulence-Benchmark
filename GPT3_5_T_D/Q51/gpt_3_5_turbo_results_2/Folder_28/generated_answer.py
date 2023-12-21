
def if_contains_anagrams(strings):
    from itertools import combinations
    from collections import Counter

    pairs = 0
    for s1, s2 in combinations(strings, 2):
        if len(s1) >= 3 and len(s2) >= 3 and s1.lower() != s2.lower():
            if Counter(s1.lower()) == Counter(s2.lower()):
                pairs += 1

    return pairs <= 78
