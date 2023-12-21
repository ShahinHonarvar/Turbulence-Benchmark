import re
def palindromes_between_indices(s):
    s = re.sub(r'[^A-Za-z]+', '', s.lower())
    return set(re.findall(r'((?=((?=.*?[a-z]))\1[a-z]+\1)', s))
