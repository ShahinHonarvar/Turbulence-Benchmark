import re
def palindromes_of_specific_lengths(s):
    m = re.findall(r'[a-z]{100,169}(?=\W\1)', s[103:-3])
    return set(m)
