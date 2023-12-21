
import re

def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)-83):
        substring = s[i:i+84]
        if re.match('^[a-zA-Z]+$', substring):
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
