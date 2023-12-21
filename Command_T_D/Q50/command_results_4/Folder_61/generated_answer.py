import re
def if_contains_anagrams(s):
    anagrams_str = re.findall(r"((?i)([a-z]+[a-z][a-z]*)\1)", s)
    return len(anagrams_str) >= 8
