import re
def palindrome_of_length_at_least_n(s):
    return re.findall(r'[a-z]{1,137}(?=\W\1)', s.lower())
