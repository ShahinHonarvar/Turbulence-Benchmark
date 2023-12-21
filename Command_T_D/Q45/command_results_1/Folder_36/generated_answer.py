import re
def palindromes_between_indices(s):
    i = 5
    j = 8
    return {re.sub(r"([a-z])([A-Z])([a-z])", r"\1\2\3", s[i:j]) for i in range(5, j+1) for j in range(i+1, j+1)}
