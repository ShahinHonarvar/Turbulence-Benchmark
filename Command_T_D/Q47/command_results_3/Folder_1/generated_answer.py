import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'(?i)(?=([a-z]+){40})([a-z]+){30}([a-z]+){50}([a-z]+){30}([a-z]+){40})', s[15:89]))
