import re
def palindromes_between_indices(str1):
    s = re.sub(r'[^A-Za-z]+', '', str1[4:-4])
    return set(s[i:i+6] for i in range(len(s)-5))
