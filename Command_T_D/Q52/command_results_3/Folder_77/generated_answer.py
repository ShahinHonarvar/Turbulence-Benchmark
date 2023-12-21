import re
def palindrome_of_length_n(s):
    return re.findall(r'[a-z]{1,173}', s.lower())
