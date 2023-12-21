import re
def palindromes_between_indices(s):
    letters = set(re.findall(r'[A-Za-z]+', s[1:-1]))
    return {s[i:j] for i in range(1, len(s)-7) for j in range(i+8, len(s))}
