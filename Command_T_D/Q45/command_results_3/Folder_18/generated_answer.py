import re
def palindromes_between_indices(s):
    return re.findall(r"((?=.)(?!\1)[a-z]{3}(?=\1))", s)
