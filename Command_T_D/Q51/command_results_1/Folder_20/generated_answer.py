import collections
import re
def if_contains_anagrams(s):
    c = collections.Counter(s)
    return all(c[k] <= 1 for k in c)
