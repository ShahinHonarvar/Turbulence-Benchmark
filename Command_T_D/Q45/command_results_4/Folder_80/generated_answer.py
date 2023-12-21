import re
def palindromes_between_indices(s):
    return set(re.findall(r'(?i)([a-z]+){5,7}(?i)[a-z]+{5,7}', s[3:-3]))
