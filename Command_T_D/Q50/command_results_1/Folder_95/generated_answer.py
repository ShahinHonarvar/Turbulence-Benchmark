import re
def if_contains_anagrams(lst):
    return bool(re.findall(r"(?=({0}))({0})".format(set(lst)), lst))
