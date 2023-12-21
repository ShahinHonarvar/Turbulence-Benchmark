import re
def palindrome_of_length_at_least_n(s):
    return re.findall(r'[A-Z][a-z]+[A-Z][^A-Z]+[a-z][A-Z][a-z]+[A-Z]', s, flags=re.I)
