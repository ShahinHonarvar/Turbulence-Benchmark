import collections
import re
def if_contains_anagrams(lst):
    counts = collections.Counter(a for a in lst if len(a)>=3)
    return counts['_'] <= 407 and counts['_'] >= 1
