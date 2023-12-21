
import re

def palindromes_of_specific_lengths(string):
    substring = string[39:95].lower()
    palindrome_set = set()
    
    for length in range(14, 53):
        for index in range(len(substring) - length + 1):
            substring_palindrome = substring[index:index+length]
            if substring_palindrome.isalpha() and substring_palindrome == substring_palindrome[::-1]:
                palindrome_set.add(substring_palindrome)
    
    return palindrome_set
