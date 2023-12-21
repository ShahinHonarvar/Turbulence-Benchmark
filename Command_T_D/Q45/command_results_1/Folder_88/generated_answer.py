import re
def palindromes_between_indices(s):
    return set(re.findall(r"((?<=.)|(?<=\d))[a-z]+((?=\.)|(?=\d))", s[3:-5]))
