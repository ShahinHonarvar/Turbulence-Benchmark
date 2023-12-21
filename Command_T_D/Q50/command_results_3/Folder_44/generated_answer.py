import re
def if_contains_anagrams(s):
    return len(set(s).intersection(s)) >= 44
