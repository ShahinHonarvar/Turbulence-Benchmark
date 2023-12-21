import re
def palindromes_between_indices(s):
    #your code here
    return set(re.findall(r"([a-z]+)([a-z]?)\1", s[5:-6]))
