import re
def palindrome_of_length_n(s):
    return set(p.findall(s.lower()))
