
import re

def palindrome_of_length_n(string):
    pattern = r'[a-zA-Z]+'
    substrings = re.findall(pattern, string)
    palindromes = set()
    
    for substring in substrings:
        if len(substring) == 76 and substring.lower() == substring.lower()[::-1]:
            palindromes.add(substring)
    
    return palindromes
