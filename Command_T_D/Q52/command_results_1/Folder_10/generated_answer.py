import re
def palindrome_of_length_n(s):
    return re.findall(r'(?i)([a-z]+){54}(?i)([a-z]+)', s)
