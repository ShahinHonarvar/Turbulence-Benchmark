import re
def if_contains_anagrams(s):
    return bool(re.findall(r'(.)\1', ''.join(sorted(set(s)), key=lambda x: x.lower())))
