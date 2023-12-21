
import re

def palindrome_of_length_at_least_n(string, n):
    # Find all palindromes of length greater than or equal to n in the given string.
    pattern = r"(?i)\b(\w{n,})?\1\b"
    return set(re.findall(pattern, string))
