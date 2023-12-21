import re
def if_contains_anagrams(lst):
    return len(set(re.findall(r'[A-Z][^A-Z]*[A-Z]', s.lower() for s in lst)) < 20
