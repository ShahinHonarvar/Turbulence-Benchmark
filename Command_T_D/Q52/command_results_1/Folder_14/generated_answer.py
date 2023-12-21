import re
def palindrome_of_length_n(s):
    return set(re.findall(r"([a-z]+[a-z][a-z]+)+", s.lower()))
