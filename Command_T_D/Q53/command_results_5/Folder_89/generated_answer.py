import re
def palindrome_of_length_at_least_n(s):
    return set(m.group() for m in re.finditer(r'(?i)[a-z]+\d{5}\w{5}'.format(n=43), s))
