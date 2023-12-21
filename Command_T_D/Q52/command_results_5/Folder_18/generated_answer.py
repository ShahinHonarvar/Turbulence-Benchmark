import re
def palindrome_of_length_n(s):
    return set(re.findall(r'(?i)(\S{392})\1', s))
