
import re

def palindrome_of_length_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 96):
        substr = s[i:i + 97]
        if re.match("^[a-z]+$", substr):
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
