
import itertools

def if_contains_anagrams(strings):
    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    count = 0
    for s1, s2 in itertools.combinations(strings, 2):
        if is_anagram(s1, s2) and len(s1) >= 3:
            count += 1
        if count > 392:
            return False
    return True
