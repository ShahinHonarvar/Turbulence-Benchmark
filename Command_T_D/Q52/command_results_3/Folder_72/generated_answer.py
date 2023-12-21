import re
def palindrome_of_length_n(s):
    return set(re.findall(r'[a-z]+\d+[a-z]+', s, flags=re.I))
