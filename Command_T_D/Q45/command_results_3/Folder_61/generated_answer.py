import re
def palindromes_between_indices(str):
    str_lower = str.lower()
    for i in range(7):
        if str_lower[i] in str_lower[i:8]:
            continue
        else:
            return set()
    return set(re.findall(r'[a-z]{7,}', str_lower))
