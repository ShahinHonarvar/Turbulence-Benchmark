
import re

def palindromes_of_specific_lengths(string):
    substr = string[41:90]
    substr = "".join([char.lower() for char in substr if char.isalpha()])
    palindromes = set()

    for length in range(23, 39):
        for i in range(len(substr) - length + 1):
            substring = substr[i : i+length]
            if substring == substring[::-1]:
                palindromes.add(substring)

    return palindromes
