import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'(?i)(?=([a-z]{35,41})))([a-z]{35,41})', s[32:-1]))
