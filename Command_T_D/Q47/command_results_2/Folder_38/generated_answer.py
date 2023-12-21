import re
def palindromes_of_specific_lengths(str):
    return set(re.findall(r'(?=([a-z]){38}(?:[a-z]+){31})[a-z]+[a-z]{61}[a-z]{31}([a-z]){38})', str[18:87]))
