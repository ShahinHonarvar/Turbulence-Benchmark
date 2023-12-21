import re
def palindromes_between_indices(s):
    str_len = len(s)
    str_low = str_len - 7
    str_high = str_low + 7
    return set(re.findall(r'[a-z]+[a-z]+', s[str_low:str_high]))
