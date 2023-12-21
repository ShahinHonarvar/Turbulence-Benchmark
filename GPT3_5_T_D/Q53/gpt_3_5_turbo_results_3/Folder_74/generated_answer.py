
import re

def palindrome_of_length_at_least_n(string):
    pattern = r'\b[a-zA-Z]{57,}\b'
    palindromes = set(re.findall(pattern, string.lower()))
    return palindromes
