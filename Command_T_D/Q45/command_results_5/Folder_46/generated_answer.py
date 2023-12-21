import re
def palindromes_between_indices(s):
    return re.findall(r'[a-z]+\d+[a-z]+', s[4:-4])
