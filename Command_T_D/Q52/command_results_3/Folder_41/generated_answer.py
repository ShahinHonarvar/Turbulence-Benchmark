import re
def palindrome_of_length_n(s):
    return re.findall(r"[a-z]+\d+[a-z]+" + str(60), s.lower())
