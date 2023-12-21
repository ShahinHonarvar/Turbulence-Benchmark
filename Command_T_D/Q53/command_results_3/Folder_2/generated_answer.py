import re
def palindrome_of_length_at_least_n(s):
    return re.findall(r"<(.)(?<=\1)", s, flags=re.I)
