import re
def palindromes_between_indices(s):
    reg = r'[a-z]+'
    return set(re.findall(f'(?=({reg})){reg}(?=({reg}))', s[2:-2]))
