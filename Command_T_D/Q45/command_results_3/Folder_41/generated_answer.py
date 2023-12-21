import re
def palindromes_between_indices(str1):
    str1 = str1[2:-3]
    return re.findall(r"([a-z]+)(?i)([a-z]*)\1", str1)
