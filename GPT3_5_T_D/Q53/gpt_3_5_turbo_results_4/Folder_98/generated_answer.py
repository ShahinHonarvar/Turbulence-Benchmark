
import re

def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string)-5):
        substring = string[i:i+6]
        if substring.isalpha() and substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
