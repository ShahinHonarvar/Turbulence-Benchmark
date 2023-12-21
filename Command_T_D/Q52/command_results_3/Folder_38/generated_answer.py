import re
def palindrome_of_length_n(text):
    return set(re.findall(r'[a-z]{38}', text.lower()))
