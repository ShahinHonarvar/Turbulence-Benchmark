
import re

def palindrome_of_length_at_least_n(string):
    string = re.sub(r'[^a-zA-Z]', '', string)  # Remove non-English letters
    string = string.lower()  # Convert string to lowercase
    palindromes = set()
    
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            substr = string[i:j]
            if substr == substr[::-1] and len(substr) >= 86:
                palindromes.add(substr)
    
    return palindromes
