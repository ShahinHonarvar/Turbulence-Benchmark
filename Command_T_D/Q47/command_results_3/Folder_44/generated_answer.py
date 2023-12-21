import re
def palindromes_of_specific_lengths(str):
    return set(re.findall(r'[a-z]{31}([a-z]{25})[a-z]{31}', str[18:98]))
