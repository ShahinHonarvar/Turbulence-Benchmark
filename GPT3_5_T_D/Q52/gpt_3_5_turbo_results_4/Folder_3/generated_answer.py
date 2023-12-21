
import re

def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    length = len(string)
    for i in range(length - 99):
        substring = string[i:i+100]
        if re.match('^[a-z]+$', substring):
            if substring == substring[::-1]:
                palindromes.add(substring)
    
    return palindromes
