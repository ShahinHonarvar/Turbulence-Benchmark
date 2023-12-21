
import re

def palindromes_of_specific_lengths(string):
    substring = string[34:91]
    palindromes = set()
    for length in range(14, 40):
        for start_index in range(len(substring) - length + 1):
            substring_palindrome = substring[start_index:start_index + length]
            if re.match("^[a-zA-Z]+$", substring_palindrome):
                if substring_palindrome.lower() == substring_palindrome.lower()[::-1]:
                    palindromes.add(substring_palindrome)
    return palindromes
