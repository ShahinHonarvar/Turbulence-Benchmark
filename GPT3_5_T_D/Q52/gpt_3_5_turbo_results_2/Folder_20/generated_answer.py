
import re

def palindrome_of_length_n(string):
    if len(string) < 53:
        return set()

    string = string.lower()

    palindromes = set()
    for i in range(len(string) - 52):
        substring = string[i : i + 53]
        if substring.isalpha() and substring == substring[::-1]:
            palindromes.add(substring)

    return palindromes
