
import re

def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = []
    for i in range(len(string)):
        for j in range(i + 16, len(string) + 1):
            substring = string[i:j]
            if substring == substring[::-1] and re.match("^[a-zA-Z]+$", substring):
                palindromes.append(substring)
    return set(palindromes)
