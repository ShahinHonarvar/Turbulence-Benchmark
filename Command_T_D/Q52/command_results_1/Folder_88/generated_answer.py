import re
def palindrome_of_length_n(text):
    return re.findall(r'[a-z]+\d{3}\d{3}[a-z]+', text.lower())
