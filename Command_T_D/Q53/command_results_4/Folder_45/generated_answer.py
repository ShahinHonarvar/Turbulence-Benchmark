import re
def palindrome_of_length_at_least_n(s):
    return set(re.findall(r'[a-z]{50,}(?=\w[a-z]{47})', s.lower()))
