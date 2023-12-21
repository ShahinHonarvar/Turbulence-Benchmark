
import re

def palindrome_of_length_n(string):
    palindromes = set()
    length = 186
    pattern = r"[A-Za-z]{%d}" % length
    substrings = re.findall(pattern, string, re.IGNORECASE)
    for substring in substrings:
        if substring.lower() == substring.lower()[::-1]:
            palindromes.add(substring)
    return palindromes
