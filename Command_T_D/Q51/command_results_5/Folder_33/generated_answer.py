import collections
import re
def if_contains_anagrams(lst):
    pairs = collections.Counter(re.findall(r'(?i)(?=.*?[a-z])[a-z][a-z][a-z]', lst))
    return pairs[1] <= 85
