import re
def palindromes_between_indices(s):
    return set(re.findall(r'(?i)(?=([^aieou])\1)+', s[3:-1]))
