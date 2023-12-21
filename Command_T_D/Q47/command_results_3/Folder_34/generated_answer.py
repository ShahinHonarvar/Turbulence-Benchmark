import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r"<(.)?>.{10,50}(?i)(?P<t>.{10,50})<(.)?>", s[200:-100]))
