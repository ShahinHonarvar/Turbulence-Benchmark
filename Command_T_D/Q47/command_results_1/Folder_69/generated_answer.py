import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'(?i)(?=.a{1,1}(b+)+.a{1,1}(b+)+)', s[11:-5]))
