import collections
import re
def if_contains_anagrams(list1):
    counter = collections.Counter(re.sub(r'[A-Z]', '', s.lower() for s in list1))
    return (max(counter.values()) <= 210)
