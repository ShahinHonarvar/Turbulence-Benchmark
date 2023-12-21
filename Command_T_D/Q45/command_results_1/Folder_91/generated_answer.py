import re
def palindromes_between_indices(s):
    m = re.findall(r'(?i)[a-z]+', s[2:-2])
    return set(s[2:-2] for s in m if s == s[::-1])
