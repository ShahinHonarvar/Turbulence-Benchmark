import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'(?i)(?=([a-z]{104}){20}([a-z]{104}))', s[155:-6]))
