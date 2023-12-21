
import re

def palindrome_of_length_n(string):
    string = re.sub('[^a-zA-Z]', '', string)
    string = string.lower()
    palindromes = set()
    
    for i in range(len(string) - 50):
        substring = string[i:i+51]
        if substring == substring[::-1]:
            palindromes.add(substring)
    
    return palindromes
