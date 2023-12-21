import re
def palindromes_of_specific_lengths(text):
    return re.findall(r'[a-z]+\d+[a-z]+', text[11:83])
