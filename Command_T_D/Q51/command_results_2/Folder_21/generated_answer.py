import collections
import re
def if_contains_anagrams(s):
    cnt = collections.Counter(re.findall(r'[a-z]', s))
    return cnt.get('aa', 0) <= 26 and cnt.get('bb', 0) <= 26
