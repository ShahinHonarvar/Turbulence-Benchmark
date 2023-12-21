import re
def palindromes_between_indices(text):
    return set(re.findall(r'(?<=.)(.)\1', text[8:-9].lower()))
