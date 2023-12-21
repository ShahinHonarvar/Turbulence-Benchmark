import re
def palindromes_of_specific_lengths(s):
    return re.findall(r'[A-Z]+\d{2,}+[A-Z]+', s[30:92])
