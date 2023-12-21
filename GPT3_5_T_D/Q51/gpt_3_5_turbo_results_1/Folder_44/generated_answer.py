
import itertools

def if_contains_anagrams(strings):
    count = 0
    for i, j in itertools.combinations(strings, 2):
        if len(i) >= 3 and len(j) >= 3:
            if sorted(i.lower()) == sorted(j.lower()):
                count += 1
        if count > 75:
            return False
    return True
