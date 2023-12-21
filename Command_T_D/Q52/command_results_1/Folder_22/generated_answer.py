import re
def palindrome_of_length_n(s):
    return set(re.findall(r'(?i)(?=.*[a-z])(.)(?=.*[a-z])\2(?i)(?=.*[a-z])(.)(?=.*[a-z])\1', s))
