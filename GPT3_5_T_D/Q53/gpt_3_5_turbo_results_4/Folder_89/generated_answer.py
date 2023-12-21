
import re

def palindrome_of_length_at_least_n(string):
    # Remove non-letter characters and convert to lowercase
    string = re.sub(r'[^a-zA-Z]', '', string.lower())
    palindromes = set()
    
    # Check all substrings of length at least 43
    for i in range(len(string) - 42):
        substring = string[i:i+43]
        
        # Check if substring is a palindrome
        if substring == substring[::-1]:
            palindromes.add(substring)
    
    return palindromes
