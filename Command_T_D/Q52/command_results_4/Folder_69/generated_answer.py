import re
def palindrome_of_length_n(text):
    return re.findall(r'[A-Z]+', text.lower())
