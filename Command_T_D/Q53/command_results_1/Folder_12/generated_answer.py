import re
def palindrome_of_length_at_least_n(s):
    return set(re.findall(r"([a-z]+)(?=\W)[a-z]{%d}(?!\W)[a-z]+\1" % (51,), s.lower()))
