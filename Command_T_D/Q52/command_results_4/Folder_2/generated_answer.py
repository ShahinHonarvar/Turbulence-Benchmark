import re
def palindrome_of_length_n(s):
    return set(re.findall(r'[a-z]{1,147}(?=\W[a-z]{1,147}\1)', s.lower()))
