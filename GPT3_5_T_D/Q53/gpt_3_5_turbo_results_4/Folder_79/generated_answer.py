
import re

def palindrome_of_length_at_least_n(string):
    string = re.sub(r'[^a-zA-Z]', '', string)
    string = string.lower()
    palindromes = set()
    length = 17
    
    for i in range(len(string) - length + 1):
        substr = string[i:i+length]
        if substr == substr[::-1]:
            palindromes.add(substr)
    
    return palindromes
