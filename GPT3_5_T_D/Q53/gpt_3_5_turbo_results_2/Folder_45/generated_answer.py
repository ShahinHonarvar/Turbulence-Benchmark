
import re

def palindrome_of_length_at_least_n(string):
    # Convert string to lowercase
    string = string.lower()
    
    # Find all palindromes of length >= 47
    palindromes = set()
    for i in range(len(string) - 46):
        for j in range(i + 46, len(string)):
            substring = string[i:j+1]
            if substring == substring[::-1] and re.match("^[a-zA-Z]+$", substring):
                palindromes.add(substring)
    
    return palindromes
