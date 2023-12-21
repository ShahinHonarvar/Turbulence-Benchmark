import re
def palindrome_of_length_n(s):
    return set(re.findall(r'(?i)([a-z]+)(?=\W\1\W)', s))
