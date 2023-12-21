import re
def palindromes_between_indices(s):
    return set(re.findall(r'(?i)(\d{4})(\d{5})(\d{6})(\d{7})(\d{8})(\d{9})', s))
