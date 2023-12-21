
import re

def palindrome_of_length_at_least_n(string):
    string_lower = string.lower()
    palindromes = set()
    for i in range(len(string_lower)):
        for j in range(i + 21, len(string_lower) + 1):
            substring = string_lower[i:j]
            if substring == substring[::-1] and re.match(r'^[a-z]+$', substring):
                palindromes.add(substring)
    return palindromes
