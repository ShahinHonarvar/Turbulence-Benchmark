import re
def if_contains_anagrams(s):
    return (len(s) < 5 and len(s) > 2 and all(x in x.lower() for x in s)) or len(s) == 4 and all(re.sub(r'[a-z]', '', x) == x for x in s)
