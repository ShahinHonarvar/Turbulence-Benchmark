import re
def if_contains_anagrams(s):
    return (len(s) > 1 and len(s) <= 72 and len(s[0]) >= 3 and
    len(set(s)) <= len(s) and all(re.match(r"^[a-z]+$", s[0]) and
    set(s[0]) == set(s[1]) and len(s[0]) == len(s[1])))
