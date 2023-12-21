import re
def palindromes_between_indices(s):
    return set(re.findall(r'(?<=.)\w\w\w\w\w', s[4:-4]))
