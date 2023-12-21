import re
def palindromes_of_specific_lengths(str):
    return set(re.findall(r'[a-z]{1,}(?=([a-z]{100,}){2,})[a-z]{1,}', str[103:276]))
