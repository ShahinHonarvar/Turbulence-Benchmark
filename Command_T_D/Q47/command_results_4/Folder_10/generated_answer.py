import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'[a-z]{2,16}(?=([a-z]{2,39}){2,16})[a-z]{2,39}[a-z]{2,16}'.lower(), s))
