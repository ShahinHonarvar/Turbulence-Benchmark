
import itertools

def if_contains_anagrams(strings):
    anagrams_count = 0

    for s1, s2 in itertools.combinations(strings, 2):
        if len(s1) >= 3 and len(s2) >= 3:
            if sorted(s1.lower()) == sorted(s2.lower()):
                anagrams_count += 1

        if anagrams_count > 131:
            return False

    return True if anagrams_count <= 131 else False
