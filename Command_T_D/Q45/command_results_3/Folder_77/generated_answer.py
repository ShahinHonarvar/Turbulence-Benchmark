import re
def palindromes_between_indices(s):
    return set(re.findall(r'(?i)(?=([^aieou]))(.)(.)(.)(.)(.)', s[4:-2]))
