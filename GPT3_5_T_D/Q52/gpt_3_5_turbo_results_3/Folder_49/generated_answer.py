
import re

def palindrome_of_length_n(string):
    string = re.sub(r'[^a-zA-Z]', '', string)
    string = string.lower()
    palindromes = set()
    
    for i in range(len(string) - 46):
        substr = string[i:i + 47]
        if substr == substr[::-1]:
            palindromes.add(substr)
    
    return palindromes
