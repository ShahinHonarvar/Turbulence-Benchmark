import re
def if_contains_anagrams(s):
    res = re.findall(r'(?i)(?=([a-z]+){2})([a-z]+)', s)
    return len(res) >= 88
