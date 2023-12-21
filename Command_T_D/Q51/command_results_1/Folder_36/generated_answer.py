import re
def if_contains_anagrams(s):
    if len(s) < 3:
        return False
    s = set(s)
    if len(s) > 26:
        return False
    return not re.search(r'(?i)(?<=.)\1(?=.)', s)
