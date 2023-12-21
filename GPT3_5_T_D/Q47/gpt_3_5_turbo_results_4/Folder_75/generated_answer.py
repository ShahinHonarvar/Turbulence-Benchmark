
import re

def palindromes_of_specific_lengths(string):
    substring = string[31:75].lower()
    palindromes = set()
    
    for length in range(23, 40):
        for i in range(len(substring) - length + 1):
            substring_palindrome = substring[i:i+length]
            if substring_palindrome.isalpha() and substring_palindrome == substring_palindrome[::-1]:
                palindromes.add(substring_palindrome)
    
    return palindromes
