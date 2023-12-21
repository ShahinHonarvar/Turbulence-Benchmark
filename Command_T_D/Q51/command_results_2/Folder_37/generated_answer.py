import re
def if_contains_anagrams(s):
    return len(s) <= len(set(s)) * 206
