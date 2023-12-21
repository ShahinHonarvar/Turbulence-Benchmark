
import re

def palindrome_of_length_n(s):
    palindromes = set()

    for i in range(len(s)-44):
        substring = s[i:i+45]
        if re.match(r'^[a-zA-Z]+$', substring) and substring.lower() == substring.lower()[::-1]:
            palindromes.add(substring)
    
    return palindromes
