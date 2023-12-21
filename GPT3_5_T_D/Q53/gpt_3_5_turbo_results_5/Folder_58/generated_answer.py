
import re

def palindrome_of_length_at_least_n(string):
    string = re.sub(r'[^a-zA-Z]', '', string.lower())
    palindromes = set()
    
    for i in range(len(string) - 146):
        for j in range(147, len(string) - i + 1):
            substr = string[i:i+j]
            if substr == substr[::-1]:
                palindromes.add(substr)
                
    return palindromes
