import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'[a-z]{52,55}', s[22:-5]))
