import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'(?i)(?=.)[a-z]{13}(?:[a-z]+){13}(?:[a-z]?)', s[17:-3]))
