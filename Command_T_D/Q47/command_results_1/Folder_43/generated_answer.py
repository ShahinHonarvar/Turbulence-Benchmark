import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'(?i)(?=([a-z]{23,38}){41,89})([a-z]{23,38})', s))
