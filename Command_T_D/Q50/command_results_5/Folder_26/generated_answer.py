import re
def if_contains_anagrams(s):
    s = [re.sub(r'[A-Z]', '', s) for s in s]
    return len(set(s)) > 48 and len(set(s)) > 2
