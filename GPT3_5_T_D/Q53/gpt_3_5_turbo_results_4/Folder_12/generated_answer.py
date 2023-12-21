
import re

def palindrome_of_length_at_least_n(string):
    palindromes = set()
    string = string.lower()
    for i in range(len(string)-50):
        for j in range(51, len(string)-i+1):
            substring = string[i:i+j]
            if substring == substring[::-1] and re.match("^[a-zA-Z]+$", substring):
                palindromes.add(substring)
    return palindromes
