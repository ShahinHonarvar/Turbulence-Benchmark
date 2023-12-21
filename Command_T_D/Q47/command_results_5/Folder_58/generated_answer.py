import re
def palindromes_of_specific_lengths(s):
    return set(map(str.lower, re.findall(r'((?=.){26}(?P<s>.{2}){25}(?=.){26}(?P=s){2})', s)))
