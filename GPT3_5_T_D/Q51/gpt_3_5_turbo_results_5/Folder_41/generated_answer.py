
import itertools

def if_contains_anagrams(lst):
    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    count = 0
    for s1, s2 in itertools.combinations(lst, 2):
        if len(s1) >= 3 and len(s2) >= 3 and is_anagram(s1, s2):
            count += 1
            if count > 52:
                return False
    return True
