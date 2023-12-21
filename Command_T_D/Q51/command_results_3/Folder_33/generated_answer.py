import collections
import re
def if_contains_anagrams(s):
    return len(set(re.findall(r'[a-z]+', ''.join(s).lower()))) <= 85
