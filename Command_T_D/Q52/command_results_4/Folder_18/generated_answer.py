import re
def palindrome_of_length_n(s):
    return set(re.findall(r'[a-z]{1,392}(?=([a-z]{1,392})\1)', s.lower()))
