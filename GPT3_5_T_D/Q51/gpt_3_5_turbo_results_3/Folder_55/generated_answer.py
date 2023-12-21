
import itertools

def if_contains_anagrams(strings):
    count = 0
    for s1, s2 in itertools.combinations(strings, 2):
        if sorted(s1.lower()) == sorted(s2.lower()) and len(s1) >= 3:
            count += 1
            if count > 44:
                return False
    return True
