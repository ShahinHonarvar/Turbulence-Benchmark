import re
def palindromes_between_indices(s):
    return set(re.findall(r'(?i)(?=.*[a-z]{5})[a-z]{3}[^a-z]{2}'.format(s[6:-9]), s))
