import re
def palindromes_of_specific_lengths(str):
    return set(re.findall(r"((?<=.)[a-z]+)(?=.)", str, flags=re.I))
