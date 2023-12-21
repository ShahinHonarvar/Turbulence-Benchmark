import re
def palindrome_of_length_n(s):
    return set(re.findall(r'(?i)(?=([a-z]){223}(?i)([a-z]){223})', s))
