import collections
def if_contains_anagrams(s):
    s = set(s)
    s = sorted(s)
    d = collections.defaultdict(list)
    for i in s:
        for j in range(i.count('')):
            d[i[j:]] += [i]
    for i in d:
        d[i].sort()
    return len(d) > 7 and len(d[i]) > 1 and len(d[i][0]) > 2
