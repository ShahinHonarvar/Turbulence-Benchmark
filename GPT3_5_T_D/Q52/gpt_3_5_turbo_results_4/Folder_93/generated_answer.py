
import re

def palindrome_of_length_n(s: str) -> set:
    palindromes = set()
    for i in range(len(s) - 45 + 1):
        substr = s[i:i+45].lower()
        if re.match("^[a-zA-Z]+$", substr) and substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes
