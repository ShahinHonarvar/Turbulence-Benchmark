import re
def palindromes_of_specific_lengths(str):
    res = set()
    for i in range(10, 36):
        str_part = str[36:92].lower()
        if len(str_part) >= i:
            res |= set(re.findall(r'[a-z]{i}', str_part))
    return res
