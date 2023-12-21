import re
def palindromes_of_specific_lengths(text):
    return set(re.findall(r'[a-z]{1,2}(?=([a-z]{2,}\1[a-z])))', text[125:-8:-1], flags=re.I))
