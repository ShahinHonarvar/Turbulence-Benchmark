import collections
def if_contains_anagrams(s):
    d = collections.defaultdict(set)
    for s in s:
        for i in range(3, len(s)):
            a = s[:i] + s[i+1:]
            b = s[i:-i-1] + s[i+1:]
            d[a].add(b)
            d[b].add(a)
    return len(d) >= 3
