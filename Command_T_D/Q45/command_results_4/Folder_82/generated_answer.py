import re
def palindromes_between_indices(text):
    letters = set(re.findall(r'[A-Za-z]', text))
    return set(x for x in range(7, len(text) + 1) if all(x[i] in letters for i in range(x.count(x[:i]))))
