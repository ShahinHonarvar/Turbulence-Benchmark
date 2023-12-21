import re
def palindrome_of_length_at_least_n(s):
    return re.findall(r'[a-z]+\w{90}([a-z]+)', s.lower())
