import re
def palindromes_between_indices(s):
    return re.findall(r"(\w){6}(?=\w\1)", s[1:-1])
