
import re

def palindrome_of_length_at_least_n(string):
    palindromes = set()
    string = string.lower()
    words = re.findall(r'[a-z]+', string)
    
    for word in words:
        if len(word) >= 4 and word == word[::-1]:
            palindromes.add(word)
    
    return palindromes
