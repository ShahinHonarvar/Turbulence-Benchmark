import re
def palindrome_of_length_n(s):
    return set(re.findall(r"(\w){28}", s.lower()))
