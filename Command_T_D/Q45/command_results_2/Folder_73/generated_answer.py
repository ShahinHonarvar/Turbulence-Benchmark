import re
def palindromes_between_indices(str):
    return re.findall(r'[a-z]+', str[3:6])
