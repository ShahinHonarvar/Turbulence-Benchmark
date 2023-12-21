
import re

def palindromes_of_specific_lengths(string):
    substring = string[39:95]
    palindromes = set()
    for length in range(14, 53):
        for i in range(len(substring) - length + 1):
            substring_palindrome = substring[i:i+length]
            if substring_palindrome.lower() == substring_palindrome.lower()[::-1] and re.match("^[a-zA-Z]+$", substring_palindrome):
                palindromes.add(substring_palindrome)
    return palindromes
