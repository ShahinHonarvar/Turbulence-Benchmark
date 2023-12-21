import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'(?i)(?<=\d)\w{55}(?=\d)', s[14:-14]))
