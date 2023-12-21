
import re

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for i in range(len(s)-148):
        for j in range(i+149, len(s)+1):
            substring = s[i:j]
            if substring.lower() == substring.lower()[::-1] and re.match(r'^[a-zA-Z]+$', substring):
                palindromes.add(substring)
    return palindromes
