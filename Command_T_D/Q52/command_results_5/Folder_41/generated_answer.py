import re
def palindrome_of_length_n(text):
    return set(re.findall(r'[a-z]+\Z', text, flags=re.I))
