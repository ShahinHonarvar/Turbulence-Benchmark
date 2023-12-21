
import re

def palindrome_of_length_n(string):
    palindromes = set()
    string = re.sub('[^a-zA-Z]', '', string.lower())
    n = len(string)
    
    for i in range(n - 42):
        substring = string[i:i+43]
        if substring == substring[::-1]:
            palindromes.add(substring)
    
    return palindromes
