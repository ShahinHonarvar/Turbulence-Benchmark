import re
def palindromes_between_indices(s):
    letters = re.findall(r'[a-z]', s[4:-2])
    return set(map(str.lower, ''.join(sorted(set(letters)))))
