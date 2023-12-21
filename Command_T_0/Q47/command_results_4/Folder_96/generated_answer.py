import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'[a-z]+\d{50,100}', s[100:-100]))
