
import re

def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string) - 92):
        substr = string[i:i+93]
        if re.match('^[a-zA-Z]+$', substr) and substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes
