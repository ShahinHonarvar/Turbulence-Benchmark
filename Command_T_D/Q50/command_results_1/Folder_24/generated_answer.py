import re
def if_contains_anagrams(lst):
    return len(set(re.findall(r'(?i)(\S+)', lst))) >= 65
