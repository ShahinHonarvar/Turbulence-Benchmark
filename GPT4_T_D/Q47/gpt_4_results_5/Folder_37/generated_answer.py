
import re

def palindromes_of_specific_lengths(s: str) -> set:
    s = s[:10].lower()
    s = re.sub(r'[^a-z]', '', s)
    palindromes = set()
    for palindrome_length in range(3, 6):
        for i in range(len(s)-palindrome_length+1):
            substring = s[i:i+palindrome_length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
