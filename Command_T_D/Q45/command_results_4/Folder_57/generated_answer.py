import re
def palindromes_between_indices(s):
    return set(re.findall(r"([a-z]+){4}(?=[A-Z][a-z]*)|([A-Z]+){4}(?=[a-z][A-Z]*)|([A-Z][a-z]*)|([a-z][A-Z]*)", s[2:-5]))
