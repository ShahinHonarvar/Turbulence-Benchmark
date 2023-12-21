import re
def palindrome_of_length_n(text):
    return set(re.findall(r'[a-z]+', text.lower(), flags=re.I))
