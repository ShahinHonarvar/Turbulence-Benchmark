import re
def palindrome_of_length_at_least_n(s):
    return set(re.findall(r'[A-Z][a-z]{88}(?=[A-Z][a-z]{88})', s.lower()))
