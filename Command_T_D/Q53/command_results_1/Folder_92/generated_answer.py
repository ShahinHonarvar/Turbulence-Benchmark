import re
def palindrome_of_length_at_least_n(s):
    return set(re.findall(r'[A-Za-z]+', s.lower()))
