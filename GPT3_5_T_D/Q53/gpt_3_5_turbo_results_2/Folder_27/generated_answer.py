
import re

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = s.lower()
    for n in range(100, len(s)+1):
        substrings = re.findall(r'\b[a-zA-Z]+\b', s)
        for substring in substrings:
            if len(substring) >= n and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
