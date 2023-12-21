
import re

def palindromes_of_specific_lengths(s):
    s = s[:11] if len(s) > 11 else s
    s = s.lower()
    palindromes = set()
    
    for i in range(len(s)):
        for j in range(i + 3, min(i + 6, len(s) + 1)):
            substring = s[i:j]
            if re.match(r'^[a-zA-Z]+$', substring) and substring == substring[::-1]:
                palindromes.add(substring)
    
    return palindromes
