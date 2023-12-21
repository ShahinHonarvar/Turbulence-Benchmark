import re
def palindromes_of_specific_lengths(str):
    return set(re.findall(r'[a-z]{1,2}(?:[a-z]+){1,2}', str[11:-12]))
