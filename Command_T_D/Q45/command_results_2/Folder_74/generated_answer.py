import re
def palindromes_between_indices(str):
    return set(re.findall(r'[a-z]{3}((?=\d).)+[a-z]{3}', str.lower()))
