
import re

def palindrome_of_length_n(string):
    palindromes = set()
    string = string.lower()
    for i in range(len(string)-288):
        substring = string[i:i+289]
        if re.match('^[a-zA-Z]+$', substring): # check if substring consists only of English letters
            if substring == substring[::-1]: # check if substring is a palindrome
                palindromes.add(substring)
    return palindromes
