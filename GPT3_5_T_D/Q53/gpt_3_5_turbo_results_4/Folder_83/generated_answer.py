
import re

def palindrome_of_length_at_least_n(s: str) -> set:
    s = s.lower()
    palindromes = set()
    
    for length in range(60, len(s) + 1):
        for i in range(len(s) - length + 1):
            substr = s[i:i+length]
            if substr == substr[::-1] and re.match(r'^[a-zA-Z]+$', substr):
                palindromes.add(substr)
    
    return palindromes
