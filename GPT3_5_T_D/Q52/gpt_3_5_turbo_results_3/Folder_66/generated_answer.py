
import re

def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 25 + 1):
        substring = s[i:i+25]
        if re.match('^[a-zA-Z]+$', substring):
            if substring == substring[::-1]:
                palindromes.add(substring)
    
    return palindromes
