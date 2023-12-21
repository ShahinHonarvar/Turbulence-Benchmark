import re
def palindrome_of_length_n(text):
    return re.findall(r'(?i)(?<=.)(.)\1', text, flags=re.I)
