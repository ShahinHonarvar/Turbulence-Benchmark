
import re

def palindrome_of_length_n(string):
    string = re.sub('[^a-zA-Z]', '', string.lower())
    palindromes = set()
    
    for i in range(len(string) - 337):
        substring = string[i:i+338]
        if substring == substring[::-1]:
            palindromes.add(substring)
    
    return palindromes
