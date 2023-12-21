
import re

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 63, len(s) + 1):
            substring = s[i:j]
            if re.match('^[a-zA-Z]+$', substring):
                if substring.lower() == substring.lower()[::-1]:
                    palindromes.add(substring)
    return palindromes
