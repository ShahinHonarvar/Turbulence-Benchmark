import re
def palindrome_of_length_at_least_n(s):
    return re.findall(r'[a-z]+[a-z][a-z]+', s.lower(), flags=re.IGNORECASE)
