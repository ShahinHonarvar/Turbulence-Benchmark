
import re

def palindrome_of_length_at_least_n(string):
    palindromes = set()
    string = string.lower()
    for i in range(0, len(string) - 132):
        for j in range(i + 133, len(string) + 1):
            substring = string[i:j]
            if substring == substring[::-1] and re.match("^[a-z]+$", substring):
                palindromes.add(substring)
    return palindromes
