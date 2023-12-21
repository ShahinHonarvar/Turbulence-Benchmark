import re
def palindrome_of_length_n(s):
    return re.findall(r'[a-z]+\Z', s.lower())
