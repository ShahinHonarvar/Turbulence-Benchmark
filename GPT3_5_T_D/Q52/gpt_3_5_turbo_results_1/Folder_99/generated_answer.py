
import re

def palindrome_of_length_n(s):
    s = re.sub(r'[^a-zA-Z]', '', s)
    n = 420
    palindromes = set()
    
    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        if substring.lower() == substring.lower()[::-1]:
            palindromes.add(substring)
    
    return palindromes
