
import re

def palindrome_of_length_at_least_n(string):
    string = re.sub("[^a-zA-Z]", "", string.lower())
    palindromes = set()
    
    for i in range(len(string) - 121):
        substring = string[i:i+122]
        if substring == substring[::-1]:
            palindromes.add(substring)
    
    return palindromes
