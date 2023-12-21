import re
def palindromes_between_indices(s):
    str_to_int = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', '000000111111111')
    m = re.findall(r'(.)\1', s[5:-5])
    return set(m.translate(str_to_int))
