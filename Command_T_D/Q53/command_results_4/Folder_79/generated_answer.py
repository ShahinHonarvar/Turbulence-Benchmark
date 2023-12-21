import re
def palindrome_of_length_at_least_n(s):
    return set(re.findall(r"<(.)(.)\2>", s, flags=re.I))
