
import re

def palindromes_of_specific_lengths(string):
    substr = string[32:72].lower()
    palindromes = set()
    for length in range(21, 33):
        for i in range(len(substr)-length+1):
            substr_palindrome = substr[i:i+length]
            if substr_palindrome.isalpha() and substr_palindrome == substr_palindrome[::-1]:
                palindromes.add(substr_palindrome)
    
    return palindromes
