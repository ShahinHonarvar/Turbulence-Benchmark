import re
def palindrome_of_length_at_least_n(s):
    return re.findall(r"((?=([A-Z][a-z]{2}){33}(?P<p>(([A-Z][a-z]{2})+)))", s.lower())
