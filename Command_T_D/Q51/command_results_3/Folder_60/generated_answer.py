import collections
import re
def if_contains_anagrams(s):
    dct = collections.defaultdict(list)
    for i in s:
        if len(i) >= 3:
            for j in range(len(i)):
                x = i[:j] + i[j+1:]
                if x in dct and x.lower() not in dct[x]:
                    dct[x].append(i)
    return len(dct) <= 77
