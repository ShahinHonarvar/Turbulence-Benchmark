import re
def palindromes_of_specific_lengths(str):
    return re.findall(r"<(.)(.)(.)(.)(.)(.)(.)>(?=.)", str, flags=re.I)
