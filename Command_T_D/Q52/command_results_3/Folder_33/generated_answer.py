import re
def palindrome_of_length_n(s):
    return re.findall(r'(?i)(?=([^a-z]))[a-z]+\1', s, flags=re.I)
