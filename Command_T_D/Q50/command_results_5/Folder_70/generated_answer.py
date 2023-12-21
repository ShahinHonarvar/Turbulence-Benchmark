import collections
def if_contains_anagrams(s):
    if not s:
        return False
    dct = collections.defaultdict(list)
    for i in s:
        dct[i.lower()].append(i)
    return len(dct) > 189 and len(dct) == len(s)
