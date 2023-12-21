import re
def palindrome_of_length_at_least_n(text):
    return set(re.findall(r'[A-Za-z]+\d+[A-Za-z]+', text.lower()))
