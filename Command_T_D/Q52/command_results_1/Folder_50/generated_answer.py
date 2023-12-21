import re
def palindrome_of_length_n(s):
    return set(re.findall(r'(?i)(?:[a-z]+){40}(?:[a-z]+)?'.format(40=40), s))
