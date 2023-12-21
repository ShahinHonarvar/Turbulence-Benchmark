import re
def if_contains_anagrams(s):
    return len(set(re.findall(r'(?i)(?:[a-z]){3}){}.*(?:[a-z]){3}', s))) <= 92
