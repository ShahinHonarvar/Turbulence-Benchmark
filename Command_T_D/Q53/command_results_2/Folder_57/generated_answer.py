import re
def palindrome_of_length_at_least_n(s):
    m = re.findall(r'[A-Z]+', s.upper())
    return set(m + [m[0][::-1]])
