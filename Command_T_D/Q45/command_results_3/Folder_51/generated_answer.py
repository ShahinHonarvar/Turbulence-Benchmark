import re
def palindromes_between_indices(s):
    for i in range(3, 5):
        s += s[i:i+i]
    return set(re.findall(r"((?i)[a-z]+)\1", s))
