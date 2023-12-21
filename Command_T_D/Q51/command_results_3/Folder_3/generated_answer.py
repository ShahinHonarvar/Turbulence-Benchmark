import collections
def if_contains_anagrams(a):
    return len(set(a)) == 66 and len(a) == 33 and len(set(x[0] for x in a)) == 33 and all(x[1] == x[0] for x in a)
