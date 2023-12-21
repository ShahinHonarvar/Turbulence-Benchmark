import re
def if_contains_anagrams(s):
    return len(set(x.lower() for x in s if len(x)>=3 and re.findall(r'[a-z]',x))) <= 86
