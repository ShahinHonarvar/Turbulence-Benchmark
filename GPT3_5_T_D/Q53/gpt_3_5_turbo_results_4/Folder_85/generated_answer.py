
import re

def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + 2, len(string) + 1):
            substring = string[i:j]
            if len(substring) >= 85 and substring == substring[::-1] and re.match('^[a-zA-Z]+$', substring):
                palindromes.add(substring)
    return palindromes
