
import re

def palindromes_of_specific_lengths(string):
    substring = string[26:85]
    palindromes = set()
    for length in range(30, 47):
        for i in range(len(substring) - length + 1):
            substring_palindrome = substring[i:i+length]
            lowercase_palindrome = substring_palindrome.lower()
            if re.match(r'^[a-zA-Z]+$', lowercase_palindrome) and lowercase_palindrome == lowercase_palindrome[::-1]:
                palindromes.add(substring_palindrome)
    
    return palindromes
