import re
def if_contains_anagrams(s):
    return len(re.findall(r'(?i)(?=([a-z]+[0-9])([a-z]+[0-9])([a-z]+)', s)) <= 84
