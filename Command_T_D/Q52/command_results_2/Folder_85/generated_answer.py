import re
def palindrome_of_length_n(str):
    return set(re.findall(r'[a-z]+', str.lower()))
