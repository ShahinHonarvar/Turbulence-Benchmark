
import re

def palindromes_of_specific_lengths(string):
    substring = string[17:73].lower()
    palindromes = set()
    for i in range(len(substring) - 50):
        for length in range(50, 52):
            substring_palindrome = substring[i:i+length]
            if re.match(r'^[a-zA-Z]+$', substring_palindrome[::-1]):
                palindromes.add(substring_palindrome)
    return palindromes
