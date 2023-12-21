import re
def if_contains_anagrams(s):
    return bool(re.findall(r'(?=([A-Z]\d){3}[A-Z]\d)', ''.join(sorted(s)), flags=re.I))
