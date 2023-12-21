import re
def palindrome_of_length_at_least_n(s):
    return re.findall(r"((?i)[a-z]+)(?=((?i)[a-z]+\2)", s, flags=re.I)
