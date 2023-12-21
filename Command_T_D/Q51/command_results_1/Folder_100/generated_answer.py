import re
def if_contains_anagrams(s):
    return len(re.findall(r'(?=([a-z]+[A-Z])([a-z]+[A-Z][a-z]+)+)', s)) <= 98
