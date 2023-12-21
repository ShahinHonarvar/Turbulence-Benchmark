import re
def palindrome_of_length_at_least_n(s):
    return set(m.group() for m in re.finditer(r'[a-z]{51}(?=\W|$)', s.lower()))
