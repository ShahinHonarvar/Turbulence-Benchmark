import re
def palindrome_of_length_at_least_n(s):
    return set(re.findall(r'(?i)(?=([a-z]){6}([a-z]))\1', s))
