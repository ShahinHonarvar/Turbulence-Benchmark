import collections
def if_contains_anagrams(s):
    if not s:
        return True
    st = collections.Counter(s)
    return all(st[k] == 1 for k in st)
