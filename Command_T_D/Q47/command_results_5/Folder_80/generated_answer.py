import re
def palindromes_of_specific_lengths(text):
    return set(re.findall(r'(?i)(?=([a-z]{24}|([a-z]{26}){2})\2{1,2})([a-z]{2}){1,26}([a-z]{2})\1', text[35:-3])
