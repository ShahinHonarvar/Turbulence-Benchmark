
import re

def palindromes_of_specific_lengths(string):
    substring = string[11:98]
    substring = substring.lower()
    palindromes = set()
    for length in range(29, 63):
        for i in range(len(substring) - length + 1):
            substring_check = substring[i : i + length]
            if substring_check == substring_check[::-1] and re.match("^[a-zA-Z]+$", substring_check):
                palindromes.add(substring_check)
    return palindromes
