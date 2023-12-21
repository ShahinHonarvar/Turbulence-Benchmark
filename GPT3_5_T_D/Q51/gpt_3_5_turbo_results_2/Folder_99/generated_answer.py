
import itertools

def if_contains_anagrams(strings):
    def is_anagram(s1, s2):
        if len(s1) != len(s2):
            return False
        return sorted(s1.lower()) == sorted(s2.lower())

    count = 0
    pairs = list(itertools.combinations(strings, 2))
    for pair in pairs:
        if is_anagram(pair[0], pair[1]):
            count += 1
        if count > 93:
            break

    return count <= 93
