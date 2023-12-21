
import re

def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = []

    for i in range(len(string) - 8):
        substr = string[i:i + 9]
        if substr == substr[::-1] and re.match('^[a-zA-Z]+$', substr):
            palindromes.append(substr)

    return set(palindromes)
