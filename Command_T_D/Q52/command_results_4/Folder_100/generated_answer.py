import re
def palindrome_of_length_n(text):
    return set(re.findall(r'[a-z]+\d{5}\d{5}[a-z]+', text.lower()))
