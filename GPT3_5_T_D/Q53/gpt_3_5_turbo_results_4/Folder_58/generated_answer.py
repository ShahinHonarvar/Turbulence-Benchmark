
import re

def palindrome_of_length_at_least_n(string):
    pattern = r'\b[a-zA-Z]{147,}\b'
    matches = re.findall(pattern, string, re.IGNORECASE)
    return set(matches)
