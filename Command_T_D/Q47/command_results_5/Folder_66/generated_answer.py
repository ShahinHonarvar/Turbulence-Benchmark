import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r"(([a-z]+)(?:[a-z]?)\1\1", s[32:80]))
