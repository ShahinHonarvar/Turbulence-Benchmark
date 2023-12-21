import re
def palindromes_between_indices(str):
    letters = list(re.findall(r'[a-z]+', str[1:-1]))
    return set(re.findall(r'|'.join(f'({s})' for s in letters), str))
