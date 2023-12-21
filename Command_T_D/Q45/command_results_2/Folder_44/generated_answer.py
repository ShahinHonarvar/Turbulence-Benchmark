import re
def palindromes_between_indices(s):
    letters = set(re.findall(r'[a-z]', s[2:-2]))
    return set(a for a in range(3, 8) if all(l == r for l, r in zip(a[::-1], a))) & {a + b for a in letters for b in letters}
