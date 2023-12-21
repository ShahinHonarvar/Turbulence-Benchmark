import re
def palindromes_of_specific_lengths(text):
    pat = r'(?i)([a-z]+)([a-z]+){3}([a-z]+)([a-z]+)[a-z]+'.format(min_length=38, max_length=49)
    return set(re.findall(pat, text[28:94]))
