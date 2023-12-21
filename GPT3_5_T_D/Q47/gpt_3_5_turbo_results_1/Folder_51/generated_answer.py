
import re

def palindromes_of_specific_lengths(string):
    substring = string[2:9].lower()
    valid_palindromes = set()
    for length in range(3, 5):
        for start in range(len(substring) - length + 1):
            substring_window = substring[start:start + length]
            if substring_window == substring_window[::-1] and re.match('^[a-zA-Z]+$', substring_window):
                valid_palindromes.add(substring_window)
    return valid_palindromes
