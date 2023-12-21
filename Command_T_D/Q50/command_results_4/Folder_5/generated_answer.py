import re
def if_contains_anagrams(s):
    return len(s)>=21 and len(set(s))>=2 and sum(1 for s1 in s for s2 in s if s1!=s2 and re.fullmatch(s1, s2))>=2
