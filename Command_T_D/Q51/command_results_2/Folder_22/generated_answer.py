import collections
import re
def if_contains_anagrams(s):
    cnt = collections.Counter(s)
    cnt = {k: v for k, v in list(cnt.items()) if k in re.findall(r'[a-z]+', k)}
    return len(set(cnt.keys())) <= 14 and len(set(cnt.values())) <= 14
