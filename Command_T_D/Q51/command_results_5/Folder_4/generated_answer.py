import re
def if_contains_anagrams(lst):
    return bool(re.findall(r"(\A[a-z]+[a-z]+[a-z]+)+", "".join(map(str.lower, lst))))
