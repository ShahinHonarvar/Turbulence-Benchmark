import re
def if_contains_anagrams(s):
    return len(re.findall(r'(?i)(?=([a-z]+[A-Z][a-z])))', s)) <= 98
