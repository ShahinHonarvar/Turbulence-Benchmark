
import re

def palindrome_of_length_n(string):
    string = re.sub(r'[^a-zA-Z]', '', string)
    palindromes = set()
    length = 54
    
    for i in range(len(string) - length + 1):
        substr = string[i:i+length]
        if substr.lower() == substr.lower()[::-1]:
            palindromes.add(substr)
    
    return palindromes
