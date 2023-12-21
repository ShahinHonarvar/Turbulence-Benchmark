import re
def if_contains_anagrams(lst):
    return bool(re.findall(r'(?i)(?=.*\1)', ''.join(sorted(lst))))
