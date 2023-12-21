import re
def if_contains_anagrams(s):
    return len(set(s)) <= 318 and len(set(s)) > 2 and len(re.findall(r'[a-z]+', s)) == len(s)
