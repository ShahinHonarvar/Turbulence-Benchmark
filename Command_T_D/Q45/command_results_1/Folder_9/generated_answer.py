import re
def palindromes_between_indices(s):
    return set(re.findall(r'(?<=.)(.*?)(?=.)', s[0:7].lower()))
