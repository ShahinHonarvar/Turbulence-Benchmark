import re
def if_contains_anagrams(s):
    return len(re.findall(r'(?i)([a-z])([a-z][a-z]\1)', s)) <= 475
