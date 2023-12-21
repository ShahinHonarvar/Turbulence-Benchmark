import re
def palindrome_of_length_at_least_n(s):
    return set(re.findall(r"([a-z]+)(?=\w[a-z]{%d})%1s{%d}(?=\w[a-z]{%d})%1s{%d}".format(56, 56, 56, 56), s.lower()))
