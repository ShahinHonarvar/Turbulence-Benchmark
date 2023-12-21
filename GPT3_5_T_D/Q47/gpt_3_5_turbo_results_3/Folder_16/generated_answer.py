
import re

def palindromes_of_specific_lengths(string):
    substring = string[15:87]
    substring = substring.lower()
    palindromes = set()
    
    for length in range(51, 61):
        for start in range(len(substring) - length + 1):
            substring_palindrome = substring[start:start+length]
            if substring_palindrome.isalpha() and substring_palindrome == substring_palindrome[::-1]:
                palindromes.add(substring_palindrome)
    
    return palindromes
