import itertools
def if_contains_anagrams(s):
    return sum(1 for s1,s2 in itertools.permutations(s, 2) if set(s1).intersection(s2)) >= 140
