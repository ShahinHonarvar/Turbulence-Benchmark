import re
def palindrome_of_length_at_least_n(s):
    return set(re.findall(r'[A-Z][a-z]+[A-Z][^A-Z]*[a-z][A-Z]{%d,}{%d}'.format(89, 89), s.lower()))
