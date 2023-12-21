import collections
import re
def if_contains_anagrams(s):
    anagrams = collections.Counter(a for a in s if len(a) >= 3 and re.fullmatch(r'[a-z]', a.lower()))
    return len(anagrams) <= 91
