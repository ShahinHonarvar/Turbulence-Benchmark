
import re

def palindromes_of_specific_lengths(string):
    substring = string[15:90].lower()
    palindromes = set()
    for length in range(40, 73):
        for i in range(len(substring) - length + 1):
            substring_palindrome = substring[i:i + length]
            if substring_palindrome == substring_palindrome[::-1] and re.match("^[a-zA-Z]+$", substring_palindrome):
                palindromes.add(substring_palindrome)
    return palindromes
