import re
def palindromes_between_indices(text):
    res = set(re.findall(r'(?<=.)(.)\1', text[0:6]))
    return res
