import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'(?i)(?P<palindrome>(?P<suf>...?)?\w{19}\w{19}(?P=suf)\w{19}\w{19}(?P=suf)...?)\w{19}\w{19}(?P=suf)\w{19}\w{19}(?P=suf)...?)(?P=palindrome)', s[15:72]))
