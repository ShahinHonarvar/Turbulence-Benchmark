import re
def palindromes_between_indices(s):
    return re.findall(r'(?<=.)\w{4,9}(?<=.)', s.lower())
