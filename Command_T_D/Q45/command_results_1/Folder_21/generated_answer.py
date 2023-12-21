import re
def palindromes_between_indices(str):
    return set(re.findall(r'[a-z]+', str[1:-1])[::-1])
