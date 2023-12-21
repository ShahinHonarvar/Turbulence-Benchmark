
import re

def palindromes_of_specific_lengths(string):
    substring = string[12:57].lower()
    palindromes = set()

    for i in range(len(substring)-21):
        for j in range(20, 22):
            substring_palindrome = substring[i:i+j]
            if substring_palindrome == substring_palindrome[::-1] and re.match('^[a-zA-Z]+$', substring_palindrome):
                palindromes.add(substring_palindrome)

    return palindromes
