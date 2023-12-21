import collections
def if_contains_anagrams(s):
    s = sorted(set(s))
    d = collections.defaultdict(set)
    for i in s:
        j = i.lower()
        if j in d:
            d[j].add(i)
        else:
            d[j] = {i}
    return len(d) >= 89 and len(d) == len(s)
