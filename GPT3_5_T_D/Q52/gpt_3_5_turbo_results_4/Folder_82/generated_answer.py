
import re

def palindrome_of_length_n(string):
    length = 28
    string = re.sub("[^a-zA-Z]", "", string.lower())
    palindromes = set()
    
    for i in range(len(string)-length+1):
        substring = string[i:i+length]
        
        if substring == substring[::-1]:
            palindromes.add(substring)
    
    return palindromes
