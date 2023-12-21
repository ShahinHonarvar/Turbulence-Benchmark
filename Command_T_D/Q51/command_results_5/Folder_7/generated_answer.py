import re
def if_contains_anagrams(s):
    if not s:
        return False
    if not all(type(x) == str for x in s):
        return False
    if not all(x.lower() in 'abcdefghijklmnopqrstuvwxyz' for x in s):
        return False
    if not all(len(x) >= 3 for x in s):
        return False
    return not re.findall(r'\b(.*?)(?i)([a-z]+)', s)
