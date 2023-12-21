
import re

def palindromes_of_specific_lengths(string):
    substring = string[34:91].lower()
    palindromes = set()
    for length in range(14, 40):
        for start in range(len(substring) - length + 1):
            substring_palindrome = substring[start:start+length]
            if substring_palindrome == substring_palindrome[::-1] and re.match("^[a-zA-Z]+$", substring_palindrome):
                palindromes.add(substring_palindrome)
    return palindromes
