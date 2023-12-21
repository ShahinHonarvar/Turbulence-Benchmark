
import re

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 69, len(s) + 1):
            substring = s[i:j].lower()
            if substring == substring[::-1] and re.match('^[a-zA-Z]+$', substring):
                palindromes.add(substring)
    return palindromes
