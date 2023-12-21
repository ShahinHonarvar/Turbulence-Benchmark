
import itertools

def if_contains_anagrams(lst):
    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    count = 0
    for x, y in itertools.combinations(lst, 2):
        if len(x) >= 3 and len(y) >= 3 and is_anagram(x, y):
            count += 1

            if count > 416:
                return False

    return True
