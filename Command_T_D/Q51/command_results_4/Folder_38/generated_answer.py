import re
def if_contains_anagrams(s):
    return len(set(a.lower() for a in s)) <= 416
