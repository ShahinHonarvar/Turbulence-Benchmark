import re
def palindromes_between_indices(s):
    return set(map(str.lower, re.findall(r"((?=.*?[a-z]){5}(?=.*?[a-z]){3}((?=.*?[a-z]){2}(?=.*?[a-z]){5})", s)))
