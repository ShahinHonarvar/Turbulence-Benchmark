import re
def palindrome_of_length_n(s):
    return re.findall(r'(?i)(?=([a-z]+\1))([a-z]+)(?=[a-z]+\2)', s, flags=re.I)
