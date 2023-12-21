
import re

def palindromes_of_specific_lengths(string):
    string = string.lower()
    substring = string[1:10]
    palindromes = set()
    
    for length in range(3, 8):
        for i in range(len(substring) - length + 1):
            substring_palindrome = substring[i:i+length]
            if substring_palindrome == substring_palindrome[::-1] and re.match("^[a-zA-Z]+$", substring_palindrome):
                palindromes.add(substring_palindrome)
    
    return palindromes
