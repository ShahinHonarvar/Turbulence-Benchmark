import collections
import re
def if_contains_anagrams(s):
    m = re.findall(r'(?i)([a-z])\1+', s)
    return len(m) <= 474
