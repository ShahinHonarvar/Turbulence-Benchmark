
import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    return set(re.findall(r'[a-z]{57,}', s))
