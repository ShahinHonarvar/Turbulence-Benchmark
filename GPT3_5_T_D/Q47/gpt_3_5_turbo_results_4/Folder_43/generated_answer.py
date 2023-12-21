
import re

def palindromes_of_specific_lengths(string):
    substring = string[41:90].lower()
    palindromes = set()
    for length in range(23, 39):
        for i in range(len(substring) - length + 1):
            possible_palindrome = substring[i:i+length]
            if possible_palindrome == possible_palindrome[::-1] and re.match("^[a-zA-Z]+$", possible_palindrome):
                palindromes.add(possible_palindrome)
    return palindromes
