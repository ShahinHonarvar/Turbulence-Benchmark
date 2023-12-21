import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r"([a-z]+)(?=\W[23-77][a-z]+\W[a-z]+)", s, flags=re.I))
