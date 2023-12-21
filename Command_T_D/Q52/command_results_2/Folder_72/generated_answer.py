import re
def palindrome_of_length_n(s):
    res = set(re.findall(r"([a-z]+)(?=\1\1)", s.lower()))
    return res
