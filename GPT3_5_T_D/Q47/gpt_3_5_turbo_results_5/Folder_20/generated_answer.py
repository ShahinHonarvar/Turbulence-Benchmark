
import re

def palindromes_of_specific_lengths(string):
    substring = string[20:75]
    palindromes = set()
    for length in range(36, 43):
        for i in range(len(substring) - length + 1):
            substring_palindrome = substring[i:i+length]
            if re.match("^[a-zA-Z]+$", substring_palindrome) and substring_palindrome.lower() == substring_palindrome.lower()[::-1]:
                palindromes.add(substring_palindrome)
    return palindromes
