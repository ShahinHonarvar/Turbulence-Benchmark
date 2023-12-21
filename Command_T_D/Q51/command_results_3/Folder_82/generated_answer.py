import re
def if_contains_anagrams(lst):
    return not (len(set(re.findall(r'[a-z]+', lst)) * 2 - 1) > 40
