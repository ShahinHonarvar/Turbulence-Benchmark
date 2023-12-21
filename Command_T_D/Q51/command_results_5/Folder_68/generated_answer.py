import collections
import re
def if_contains_anagrams(list1):
    return len(set(list(zip(*list(map(lambda s: (re.sub(r'[A-Z].+', '', s), s), list(range(len(s) - 2)))), key=lambda s: s)) < 94)
