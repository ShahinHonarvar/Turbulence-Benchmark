import re
def palindromes_of_specific_lengths(s):
    return set(map(str.lower,re.findall(r'(?<=\d{12})[a-z]+\d{42}\d{12}[a-z]+\d{92}(?<=\d{12})', s)))
