
import re

def palindromes_of_specific_lengths(s):
    s = s[21:63]
    palindromes = set()

    for l in range(22, 34):
        for i in range(len(s) - l + 1):
            substr = s[i: i + l]
            if substr.lower() == substr[::-1].lower() and substr.isalpha():
                palindromes.add(substr)

    return palindromes
