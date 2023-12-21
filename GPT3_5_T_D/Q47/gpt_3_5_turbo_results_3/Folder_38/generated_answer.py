
import re

def palindromes_of_specific_lengths(string):
    substring = string[18:88]

    palindromes = set()

    for length in range(38, 61):
        for i in range(len(substring) - length + 1):
            substr = substring[i:i+length]
            if substr.isalpha() and substr.lower() == substr.lower()[::-1]:
                palindromes.add(substr)

    return palindromes
