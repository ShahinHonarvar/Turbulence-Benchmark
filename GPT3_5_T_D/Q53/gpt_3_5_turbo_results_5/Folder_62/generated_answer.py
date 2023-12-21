
import re

def palindrome_of_length_at_least_n(string):
    palindromes = set()
    
    # Convert string to lowercase
    string = string.lower()
    
    # Regex pattern to find palindromes
    pattern = r'(?=(\b\w{31,}\b))'
    
    # Find all palindromes in the string
    matches = re.findall(pattern, string)
    
    for match in matches:
        palindrome = match[0]
        
        # Check if the palindrome is a valid palindrome
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    
    return palindromes
