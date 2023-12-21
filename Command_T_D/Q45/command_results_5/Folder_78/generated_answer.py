import re
def palindromes_between_indices(s):
    return set(re.findall(r'(?i)(\w){6}(?:\w){8}(?:\w){6}\w)', s))
