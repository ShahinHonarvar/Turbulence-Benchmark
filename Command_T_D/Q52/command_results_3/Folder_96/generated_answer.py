import re
def palindrome_of_length_n(s):
    return re.findall(r'[A-Z]+\d+[A-Z]+', s.lower())
