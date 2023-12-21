
import re

def palindromes_of_specific_lengths(string):
    substring = string[18:66].lower()
    palindromes = set()

    for length in range(23, 37):
        for start in range(len(substring) - length + 1):
            substring_to_check = substring[start:start+length]
            if substring_to_check.isalpha() and substring_to_check == substring_to_check[::-1]:
                palindromes.add(substring_to_check)

    return palindromes
