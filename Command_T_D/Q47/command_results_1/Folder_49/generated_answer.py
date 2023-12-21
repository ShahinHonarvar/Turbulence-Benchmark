import re
def palindromes_of_specific_lengths(s):
    return {m.group() for m in re.finditer(r'(?i)(?P<palindrome>(?P<initial>[a-z]){10,50}(?P<final>[a-z])\1)', s[10:-10])}
