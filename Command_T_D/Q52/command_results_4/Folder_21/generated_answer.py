import re
def palindrome_of_length_n(text):
    return re.findall(r'[a-z]+', text.lower(), flags=re.I)
