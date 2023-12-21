import re
def palindromes_of_specific_lengths(text):
    return re.findall(r'(?i)([a-z]+)[a-z]+'.upper(), text[22:95])
