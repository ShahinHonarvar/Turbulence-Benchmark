import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'(?i)(?=((?<=[^aieou])\1)+)', s[10:75]))
