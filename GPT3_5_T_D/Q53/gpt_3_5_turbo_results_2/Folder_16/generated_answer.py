
import re

def palindrome_of_length_at_least_n(string):
    n = 119
    pattern = r'\b\w{' + str(n) + r',}\b'
    matches = set(re.findall(pattern, string, flags=re.I))
    palindromes = set(filter(lambda x: x.lower() == x.lower()[::-1], matches))
    return palindromes
