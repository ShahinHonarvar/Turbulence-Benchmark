import re
def palindrome_of_length_n(s):
    return set(re.findall(r'(?=.)(.)\1', s.lower()))
