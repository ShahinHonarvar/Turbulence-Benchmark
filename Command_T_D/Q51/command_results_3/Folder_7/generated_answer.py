import re
def if_contains_anagrams(list_str):
    return bool(re.findall(r'(?i)(?=([a-z]+)\1)', '|'.join(list_str), re.I))
