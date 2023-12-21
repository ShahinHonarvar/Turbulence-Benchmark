import re
def palindromes_between_indices(s):
    return set(re.findall(r'([a-z]+)(?=\w[a-z])([a-z]*)', s[1:-1]))
