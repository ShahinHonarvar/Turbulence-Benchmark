import re
def if_contains_anagrams(s):
    return not bool(re.findall(r'(?=([a-z]+){3})([a-z]+){3}', s))
