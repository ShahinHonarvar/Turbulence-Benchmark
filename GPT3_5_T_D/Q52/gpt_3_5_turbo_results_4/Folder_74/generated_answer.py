
import re

def palindrome_of_length_n(string):
    palindromes = set()
    string = string.lower()
    
    for i in range(len(string) - 95):
        substring = string[i:i+96]
        if re.match(r'^[a-zA-Z]+$', substring):  # check if substring consists of only English letters
            if substring == substring[::-1]:  # check if substring is a palindrome
                palindromes.add(substring)
    
    return palindromes
