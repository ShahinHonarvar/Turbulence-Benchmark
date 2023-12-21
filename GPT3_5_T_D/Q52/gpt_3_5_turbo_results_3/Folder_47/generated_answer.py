
import re

def palindrome_of_length_n(string):
    string = re.sub("[^A-Za-z]", "", string.lower())
    palindromes = set()
    
    for i in range(len(string) - 33):
        substring = string[i:i+34]
        if substring == substring[::-1]:
            palindromes.add(substring)
    
    return palindromes
