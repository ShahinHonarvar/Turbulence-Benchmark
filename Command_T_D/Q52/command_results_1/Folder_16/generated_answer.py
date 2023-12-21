import re
def palindrome_of_length_n(s):
    return re.findall(r'[a-z]+', s, flags=re.I)[-1][-1]
