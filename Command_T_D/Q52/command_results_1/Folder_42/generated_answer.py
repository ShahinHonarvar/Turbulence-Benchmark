import re
def palindrome_of_length_n(s):
    return set(re.findall(r'(?i)(?=([a-z]+\1[a-z]+){278})', s))
