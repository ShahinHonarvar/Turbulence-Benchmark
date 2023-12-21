import re
def palindromes_between_indices(s):
    return set(re.findall(r"((?=.)(?P<palidrome>[a-z]){6}(?=.)\2)", s[2:-2]))
