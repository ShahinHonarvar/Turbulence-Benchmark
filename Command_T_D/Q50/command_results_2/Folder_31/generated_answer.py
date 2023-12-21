import re
def if_contains_anagrams(s):
    return bool(re.findall(r'(?i)(?=([a-z]+\d+)+[a-z]+\d+)+', ''.join(s)))
