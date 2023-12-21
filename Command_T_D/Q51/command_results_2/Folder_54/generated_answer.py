import collections
import re
def if_contains_anagrams(s):
    table = collections.Counter(s)
    if not all(table[k] == 1 for k in table):
        return False
    s = re.sub(r'([A-Z])([a-z])([A-Z])', r'\1\2\3', s)
    if len(s) < 3:
        return False
    if table[s]:
        return False
    return True
