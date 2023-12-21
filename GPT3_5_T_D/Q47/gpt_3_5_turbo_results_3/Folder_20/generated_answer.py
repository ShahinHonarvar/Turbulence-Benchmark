
import re

def palindromes_of_specific_lengths(string):
    substring = string.lower()[20:75]
    palindromes = set()

    for length in range(36, 43):
        for i in range(len(substring) - length + 1):
            substr = substring[i:i+length]
            if re.match("^[a-zA-Z]+$", substr) and substr == substr[::-1]:
                palindromes.add(substr)

    return palindromes
