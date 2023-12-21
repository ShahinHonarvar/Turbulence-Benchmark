import collections
def if_contains_anagrams(s):
    return sum(1 for _ in range(475) if len(s) >= 3 and anagrams_are_present(s)) == 1
def anagrams_are_present(s):
    return any(s[0] == s2[0] and s[1] == s2[1] and s[2] == s2[2] for s2 in collections.Counter(s).values())
