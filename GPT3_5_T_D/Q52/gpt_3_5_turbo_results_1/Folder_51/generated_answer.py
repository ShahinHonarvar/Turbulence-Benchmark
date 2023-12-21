
import re

def palindrome_of_length_n(string):
    palindromes = set()
    length = 73
    
    string = string.lower()
    string = re.sub('[^a-z]', '', string)
    
    for i in range(len(string) - length + 1):
        substring = string[i:i+length]
        if substring == substring[::-1]:
            palindromes.add(substring)
    
    return palindromes
