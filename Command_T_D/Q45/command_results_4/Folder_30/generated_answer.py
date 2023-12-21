import re
def palindromes_between_indices(str):
    idx = str.lower().find('a')
    return set(re.findall(r'([a-z]{4})\1', str[idx:idx+5]))
