import re
def palindromes_between_indices(s):
    return set(re.findall(r'(?i)(?=([^aieou]))[aieou]{7}(?=[^aieou]*$)', s[3:-9]))
