import collections
def if_contains_anagrams(s):
    c = collections.Counter(s)
    return all(c[a] == 1 for a in c if len(set(a)) == len(set(b)) for b in c)
