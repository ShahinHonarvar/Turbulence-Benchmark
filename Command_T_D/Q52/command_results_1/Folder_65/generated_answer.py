import re
def palindrome_of_length_n(s):
    return re.findall(r'(?i)(?=([a-z]){35}(?i).)*([a-z]){35}(?i))', s)
