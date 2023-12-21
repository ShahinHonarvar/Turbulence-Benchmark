import re
def palindrome_of_length_at_least_n(s):
    return re.findall(r'(?=([a-z]+\d){4}(?:[a-z]+\d){4})', s, flags=re.IGNORECASE)
