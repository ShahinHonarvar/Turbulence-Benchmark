import re
def if_contains_anagrams(s):
    s = re.findall("[A-Z][^A-Z]*[A-Z][^A-Z]*[A-Z]", s)
    if len(s) == len(set(s)):
        return True
    else:
        return False
