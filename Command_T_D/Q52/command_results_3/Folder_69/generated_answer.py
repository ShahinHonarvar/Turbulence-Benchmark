import re
def palindrome_of_length_n(s):
    return set(re.findall(r"([A-Z]+)[A-Z]+", s.lower()))
