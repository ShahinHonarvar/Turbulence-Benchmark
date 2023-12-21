
import re

def palindromes_of_specific_lengths(string):
    valid_palindromes = set()
    substring = string[100:301].lower()
    for length in range(50, 101):
        pattern = "[a-zA-Z]{" + str(length) + "}"
        matches = re.findall(pattern, substring)
        for match in matches:
            if match == match[::-1]:
                valid_palindromes.add(match)
    return valid_palindromes
