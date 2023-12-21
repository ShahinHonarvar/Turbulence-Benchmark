import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'[a-z]{1,}(?=([a-z]{2,}(?:[a-z]{1,}){2,}){1,}))', s[20:-4])
