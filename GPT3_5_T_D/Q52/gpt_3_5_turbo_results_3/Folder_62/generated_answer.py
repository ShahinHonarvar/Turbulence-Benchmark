
import re

def palindrome_of_length_n(string):
    string = re.sub('[^a-zA-Z]', '', string.lower())
    palindromes = set()
    n = 188
    length = len(string)
    
    if length < n:
        return palindromes
    
    for i in range(length - n + 1):
        substring = string[i:i+n]
        if substring == substring[::-1]:
            palindromes.add(substring)
    
    return palindromes
