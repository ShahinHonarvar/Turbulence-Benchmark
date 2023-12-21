import re
def if_contains_anagrams(s):
    return bool(re.findall(r'(?=([a-z]+){3})([a-z]+){3}(?!\1)[a-z]+', s))
