import re
def if_contains_anagrams(s):
    return not any(re.search(r'(.*?)\1', s) for s in s)
