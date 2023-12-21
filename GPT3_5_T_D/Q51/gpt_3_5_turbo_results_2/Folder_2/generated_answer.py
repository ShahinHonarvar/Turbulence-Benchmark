
def if_contains_anagrams(lst):
    from collections import Counter
    from itertools import combinations
    
    def is_anagram(s1, s2):
        return Counter(s1.lower()) == Counter(s2.lower())
    
    count = 0
    for s1, s2 in combinations(lst, 2):
        if len(s1) >= 3 and is_anagram(s1, s2):
            count += 1
            if count > 81:
                return False
    return True
