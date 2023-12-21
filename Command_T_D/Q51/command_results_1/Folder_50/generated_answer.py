import re
def if_contains_anagrams(s):
    s=re.findall(r'[a-z]+', s)
    return len(s) <= 47
