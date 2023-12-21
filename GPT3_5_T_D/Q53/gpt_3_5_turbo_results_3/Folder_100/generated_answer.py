
import re

def palindrome_of_length_at_least_n(string):
    palindromes = set()
    lowercase_string = string.lower()
    for i in range(len(lowercase_string) - 47):
        substr = lowercase_string[i:i+48]
        if re.match(r'^[a-z]+$', substr) and substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes
