import re
def palindromes_of_specific_lengths(s):
    m = re.findall(r'[a-z]+', s[127:])
    return {m[i:i+120] for i in range(len(m) - 119)}
