import re
def palindromes_of_specific_lengths(str1):
    return set(re.findall(r"<(a|A)[\d]{3}>([A-Z])[0-9][\d]?(a|A)[\d]{3}>", str1))
