import re
def palindrome_of_length_n(string):
    return set(re.findall(r'[a-z]+', string.lower()))
