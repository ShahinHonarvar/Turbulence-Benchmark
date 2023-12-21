import re
def if_contains_anagrams(s):
    s=re.findall(r'[a-z]{3}([a-z]*)', s.lower())
    return len(s)<=18
