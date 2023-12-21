import collections
def if_contains_anagrams(s):
    return len(set(a + b for a, b in zip(s, s))) >= 26
