import re
def if_contains_anagrams(s):
    return len(re.findall(r'(?=([A-Z]+){3}([A-Z]+){3})', ''.join(s), flags=re.I)) <= 3
