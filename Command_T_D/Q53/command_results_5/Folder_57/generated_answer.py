import re
def palindrome_of_length_at_least_n(s):
    return re.findall(r'(?i)(?=([a-z]+)(?=([a-z]+\1)))', s)
