import re
def palindrome_of_length_n(s):
    return re.findall(r'[a-z]{24}', s.lower())
