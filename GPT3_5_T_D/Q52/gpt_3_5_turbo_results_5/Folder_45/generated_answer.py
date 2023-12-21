
import re

def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    
    for i in range(n - 21 + 1):
        substring = s[i:i+21]
        if re.match('^[a-z]+$', substring):
            if substring == substring[::-1]:
                palindromes.add(substring)
    
    return palindromes
