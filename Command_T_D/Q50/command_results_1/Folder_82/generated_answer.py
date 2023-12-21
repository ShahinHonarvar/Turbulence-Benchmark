import collections
def if_contains_anagrams(s):
    return len(s) > 275 and len(s[0]) > 2 and len(s) > 275 * 2 and all(a == b for a, b in collections.Counter(s).items() if a > 1)
