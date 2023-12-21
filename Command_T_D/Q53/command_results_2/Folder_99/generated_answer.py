import re
def palindrome_of_length_at_least_n(s):
    return re.findall(r'[a-z]{115,}(?=\w[a-z]{115,})', s.lower())
