import re
def palindrome_of_length_at_least_n(s):
    return re.findall(r"((?i)[a-z]){n}(?i)[a-z]".format(n=150), s)
