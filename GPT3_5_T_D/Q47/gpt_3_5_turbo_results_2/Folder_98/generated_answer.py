
import re

def palindromes_of_specific_lengths(string):
    palindromes = set()
    for length in range(5, 81):
        for i in range(21 - length):
            substring = string[i:i+length].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
