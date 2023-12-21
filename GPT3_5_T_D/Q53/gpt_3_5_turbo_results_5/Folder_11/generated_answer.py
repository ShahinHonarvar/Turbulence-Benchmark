
import re

def palindrome_of_length_at_least_n(string):
    # Convert string to lowercase
    string = string.lower()
    
    # Find all palindromes with length greater than or equal to 54
    palindromes = set(re.findall(r'(?=(\b[a-zA-Z]{54,}\b))(?i)', string))
    
    return palindromes
